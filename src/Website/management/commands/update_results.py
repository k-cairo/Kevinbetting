from django.core.management.base import BaseCommand
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Website.management.commands.update_matchs_a_venir import format_championships_names, format_teams_names
from utils.constant import LIST_CHAMPIONSHIP, yesterday
from utils.selenium_functions import open_browser, accept_cookie
from Website.models import MatchsAVenir


def get_yesterday_all_matchs(date: str) -> dict[str: list[str]]:
    """
    Get all matchs played yesterday.
    :param date: Date
    :return: A dictionary with in key the date (yesterday) and in value the list of the matchs for this specific day.
    """
    all_matchs = {}
    driver = open_browser()
    driver.get(f"https://www.matchendirect.fr/resultat-foot-{date}/")
    accept_cookie(driver=driver)

    all_div_championships = driver.find_elements(By.CSS_SELECTOR, "div div.panel.panel-info")

    for div_championship in all_div_championships[:-2]:
        try:
            championship = div_championship.find_element(By.CSS_SELECTOR, "h3.panel-title a").text
        except NoSuchElementException:
            pass
        else:
            if championship in LIST_CHAMPIONSHIP:
                championship_format = format_championships_names(championship=championship)
                all_matchs[championship_format] = []
                raw_matchs = div_championship.find_elements(By.CSS_SELECTOR, "tbody td.lm3")
                for row_match in raw_matchs:
                    home_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq1").text
                    home_team_format = format_teams_names(team=home_team)
                    away_team = row_match.find_element(By.CSS_SELECTOR, "span.lm3_eq2").text
                    away_team_format = format_teams_names(team=away_team)
                    format_match = f"{home_team_format}|{away_team_format}"
                    match_link = row_match.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                    all_matchs[championship_format].append((format_match, match_link))
    return all_matchs


def get_matchs_stats(url):
    stats = {}
    total_yellow_cards = 0
    total_red_cards = 0
    total_corners = 0
    driver = open_browser()
    driver.get(url=url)
    accept_cookie(driver=driver)

    table_match_statictics = driver.find_element(By.CSS_SELECTOR, 'div.MEDpanelstats table')
    table_raws = table_match_statictics.find_elements(By.CSS_SELECTOR, 'tr')

    for table_raw in table_raws:
        table_datas = table_raw.find_elements(By.CSS_SELECTOR, 'td')
        if table_datas[2].text == "Corners":
            home_team_corners = table_datas[0].text
            away_team_corners = table_datas[4].text
            total_corners = int(home_team_corners) + int(away_team_corners)
            stats["Corners"] = total_corners

        if table_datas[2].text == "Carton jaune":
            home_team_yellow_card = table_datas[0].text
            away_team_yellow_card = table_datas[4].text
            total_yellow_cards = int(home_team_yellow_card) + int(away_team_yellow_card)

        if table_datas[2].text == "Carton rouge":
            home_team_red_card = table_datas[0].text
            away_team_red_card = table_datas[4].text
            total_red_cards = int(home_team_red_card) + int(away_team_red_card)

        stats["Cards"] = total_red_cards + total_yellow_cards

    return stats


class Command(BaseCommand):
    help = "Scrape Yesterday's matchs, Get corners and cards data and save it in database"

    def handle(self, *args, **options):
        all_matchs = get_yesterday_all_matchs(date=yesterday)

        for championship, rencontres in all_matchs.items():
            for rencontre in rencontres:
                target_match = MatchsAVenir.objects.filter(match=rencontre[0].replace('|', ' - '), date=yesterday)
                if target_match:
                    stats = get_matchs_stats(url=rencontre[1])
                    card_bet = float(target_match.get().card_bet.strip("+ "))
                    corner_bet = float(target_match.get().corner_bet.strip("+ "))

                    if stats["Corners"] > corner_bet:
                        corner_bet_passed = True
                    else:
                        corner_bet_passed = False

                    if stats["Cards"] > card_bet:
                        card_bet_passed = True
                    else:
                        card_bet_passed = False

                    print(f"{rencontre[0].replace('|', ' - ')} | Corners: {stats['Corners']} | Cards: {stats['Cards']}")

                    target_match.update(real_corners=stats["Corners"], real_cards=stats["Cards"],
                                        card_bet_passed=card_bet_passed, corner_bet_passed=corner_bet_passed)

        self.stdout.write("Yesterday's matchs datas updated")
