from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from utils.constant import today
from utils.selenium_functions import open_browser
from Website.models import Iframe, Data


def get_datas_and_update_database(url: str, championship: str, driver, data_stats: str):
    teams = get_teams(driver=driver, url=url)
    stats = get_stats(driver=driver)
    update_database(championship=championship, home_teams=teams[0], home_stats=stats[0],
                    away_teams=teams[1], away_stats=stats[1], data_stats=data_stats)


def get_teams(driver, url: str) -> (list[str], list[str]):
    """
    Parse Home Teams and Away Teams from championship iframe url.
    :param driver: Selenium Chrome Webdriver
    :param url: Championship iframe url
    :return: A tuple of home teams list and away teams list
    """
    other_teams = []
    home_teams = []

    driver.get(url)

    teams = driver.find_elements(By.CSS_SELECTOR, "tbody tr td a")
    for i, team in enumerate(teams):
        if i % 3 == 0:
            home_teams.append(team.text)
        else:
            other_teams.append(team.text)
    away_teams = [team for i, team in enumerate(other_teams) if i % 2 == 0]
    return home_teams, away_teams


def get_stats(driver) -> (list[str], list[str]):
    """
    Parse Home Teams datas and Away Teams datas from championship iframe url.
    :param driver: Selenium Chrome Webdriver
    :return: A tuple of list of datas for home teams and away teams.
    """
    home_stats = []
    away_stats = []
    all_tr = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
    for tr in all_tr[2:-1]:
        all_td = tr.find_elements(By.CSS_SELECTOR, "td")
        home_stat = all_td[4].text
        away_stat = all_td[9].text
        home_stats.append(home_stat)
        away_stats.append(away_stat)
    return home_stats, away_stats


def update_database(championship: str, home_teams: list[str], home_stats: list[str], away_teams: list[str],
                    away_stats: list[str], data_stats: str):
    """
    Update Championship datas in database if existing else create Championship datas.
    :param championship: Championship's name
    :param home_teams: List of home teams
    :param home_stats: List of home teams stats
    :param away_teams: List of away teams
    :param away_stats: List of away teams stats
    :param data_stats: Statistic name
    :return: Printing Datas creating or Datas Updating in Database
    """
    result = {
        "Home Teams": [],
        "Away Teams": []
    }

    for i, team in enumerate(home_teams):
        result["Home Teams"].append({team: home_stats[i]})

    for i, team in enumerate(away_teams):
        result["Away Teams"].append({team: away_stats[i]})

    if len(Data.objects.filter(championship=championship).filter(datas_stats=data_stats)) == 0:
        Data.objects.create(championship=championship, datas=result, datas_stats=data_stats, date_updated=today)
        return print(f"Datas created in database. Championship : {championship} | Stats : {data_stats}")
    else:
        Data.objects.filter(championship=championship).filter(datas_stats=data_stats).update(datas=result,
                                                                                             date_updated=today)
        return print(f"Datas updated in database. Championship : {championship} | Stats : {data_stats}")


class Command(BaseCommand):
    help = 'Update cards and corners Datas'

    def handle(self, *args, **options):
        driver = open_browser()

        # GET CARDS AND CORNERS IFRAMES FROM DATABASE
        cards_against_iframes = Iframe.objects.filter(iframe_stats="cards against")
        cards_for_iframes = Iframe.objects.filter(iframe_stats="cards for")
        corners_against_iframes = Iframe.objects.filter(iframe_stats="corners against")
        corners_for_iframes = Iframe.objects.filter(iframe_stats="corners for")

        # UPDATE 'CARDS FOR' DATAS
        for card_for_iframe in cards_for_iframes:
            get_datas_and_update_database(url=card_for_iframe.iframe_url, championship=card_for_iframe.championship,
                                          driver=driver, data_stats="cards for")

        # UPDATE 'CARDS AGAINST' DATAS
        for card_against_iframe in cards_against_iframes:
            get_datas_and_update_database(url=card_against_iframe.iframe_url,
                                          championship=card_against_iframe.championship,
                                          driver=driver, data_stats="cards against")

        # UPDATE 'CORNERS FOR' DATAS
        for corner_for_iframe in corners_for_iframes:
            get_datas_and_update_database(url=corner_for_iframe.iframe_url, championship=corner_for_iframe.championship,
                                          driver=driver, data_stats="corners for")

        # UPDATE 'CORNERS AGAINST' DATAS
        for corner_against_iframe in corners_against_iframes:
            get_datas_and_update_database(url=corner_against_iframe.iframe_url,
                                          championship=corner_against_iframe.championship,
                                          driver=driver, data_stats="corners against")

        self.stdout.write('Cards and Corners Datas Updated Successfully')
