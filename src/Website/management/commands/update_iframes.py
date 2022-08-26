from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By
from utils.constant import CARDS, CORNERS, LEAGUES_URLS, TEAMS_IN_CHAMPIONSHIP, today
from utils.selenium_functions import open_browser
from Website.models import Iframe


def get_all_cards_iframes(driver) -> (dict[str: str], dict[str: str]):
    """
    Get all cards statistic iframes
    :param driver: Selenium Chrome Webdriver
    :return: A tuple of dictionary for cards for and cards against statistic. Championship in key, iframe link in value
    """
    iframes_yc_for = {}
    iframes_yc_against = {}

    for championship, url in LEAGUES_URLS.items():
        card_link = url + CARDS
        driver.get(card_link)
        nb_team = TEAMS_IN_CHAMPIONSHIP[championship]
        try:
            iframes = driver.find_elements(By.CSS_SELECTOR, f"div.embed-container{nb_team} iframe")
            iframe_yc_for = iframes[0].get_attribute('src')
            iframe_yc_against = iframes[1].get_attribute('src')
        except IndexError:
            print(f"Erreur avec le championnat : {championship} - CARDS")
        else:
            iframes_yc_for[championship] = iframe_yc_for
            iframes_yc_against[championship] = iframe_yc_against

    return iframes_yc_for, iframes_yc_against


def get_all_corners_iframes(driver) -> (dict[str: str], dict[str: str]):
    """
    Get all corners statistic iframes
    :param driver: Selenium Chrome Webdriver
    :return: A tuple of dictionary for corners for and corners against statistic.
             Championship in key, iframe link in value.
    """
    iframes_corner_for = {}
    iframes_corner_against = {}

    for championship, url in LEAGUES_URLS.items():
        corner_link = url + CORNERS
        driver.get(corner_link)
        nb_team = TEAMS_IN_CHAMPIONSHIP[championship]
        try:
            iframes = driver.find_elements(By.CSS_SELECTOR, f"div.embed-container{nb_team} iframe")
            iframe_corner_for = iframes[5].get_attribute('src')
            iframe_corner_against = iframes[6].get_attribute('src')
        except IndexError:
            print(f"Erreur avec le championnat : {championship} - CORNERS")
        else:
            iframes_corner_for[championship] = iframe_corner_for
            iframes_corner_against[championship] = iframe_corner_against

    return iframes_corner_for, iframes_corner_against


def update_card_iframe(stats: str, championship: str, iframe: str):
    """
    Update Championship's iframe link in database if existing else create Championship iframe link.
    :param stats: Statistic's name
    :param championship: Championship's name
    :param iframe: Championship's iframe link
    :return: Printing iframe link creating or iframe link updating in database
    """
    if stats == "cards for":
        if len(Iframe.objects.filter(championship=championship).filter(iframe_stats="cards for")) == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="cards for", date_updated=today)
            return print(f"Iframe link created in database. Championship : {championship} | Stats : {stats}")
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="cards for").update(
                iframe_url=iframe, date_updated=today)
            return print(f"Iframe link updated in database. Championship : {championship} | Stats : {stats}")

    elif stats == "cards against":
        if len(Iframe.objects.filter(championship=championship).filter(iframe_stats="cards against")) == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="cards against", date_updated=today)
            return print(f"Iframe link created in database. Championship : {championship} | Stats : {stats}")
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="cards against").update(
                iframe_url=iframe, date_updated=today)
            return print(f"Iframe link updated in database. Championship : {championship} | Stats : {stats}")


def update_corners_iframes(stats: str, championship: str, iframe: str):
    """
      Update Championship's iframe link in database if existing else create Championship iframe link.
      :param stats: Statistic's name
      :param championship: Championship's name
      :param iframe: Championship's iframe link
      :return: Printing iframe link creating or iframe link updating in database
      """
    if stats == "corners for":
        if len(Iframe.objects.filter(championship=championship).filter(iframe_stats="corners for")) == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe, iframe_stats="corners for",
                                  date_updated=today)
            return print(f"Iframe link created in database. Championship : {championship} | Stats : {stats}")
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="corners for").update(
                iframe_url=iframe, date_updated=today)
            return print(f"Iframe link updated in database. Championship : {championship} | Stats : {stats}")

    if stats == "corners against":
        if len(Iframe.objects.filter(championship=championship).filter(iframe_stats="corners against")) == 0:
            Iframe.objects.create(championship=championship, iframe_url=iframe,
                                  iframe_stats="corners against", date_updated=today)
            return print(f"Iframe link created in database. Championship : {championship} | Stats : {stats}")
        else:
            Iframe.objects.filter(championship=championship).filter(iframe_stats="corners against").update(
                iframe_url=iframe, date_updated=today)
            return print(f"Iframe link updated in database. Championship : {championship} | Stats : {stats}")


class Command(BaseCommand):
    help = "Get Cards and Corners Iframes. Save it in database if doesn't exist else update it in database"

    def handle(self, *args, **options):
        driver = open_browser()

        ######################################## CARDS IFRAMES ###################################################
        # GET CARDS IFRAMES
        cards_iframes = get_all_cards_iframes(driver=driver)

        # UPDATE CARDS FOR IFRAMES IN DATABASE
        for championship, iframe in cards_iframes[0].items():
            update_card_iframe(stats="cards for", championship=championship, iframe=iframe)

        # UPDATE CARDS AGAINST IFRAMES IN DATABASE
        for championship, iframe in cards_iframes[1].items():
            update_card_iframe(stats="cards against", championship=championship, iframe=iframe)

        ###################################### CORNERS IFRAMES ##################################################
        # GET CORNERS IFRAMES
        corners_iframes = get_all_corners_iframes(driver=driver)

        # UPDATE CORNERS FOR IFRAMES IN DATABASE
        for championship, iframe in corners_iframes[0].items():
            update_corners_iframes(stats="corners for", championship=championship, iframe=iframe)

        # UPDATE CORNERS AGAINST IFRAMES IN DATABASE
        for championship, iframe in corners_iframes[1].items():
            update_corners_iframes(stats="corners against", championship=championship, iframe=iframe)

        self.stdout.write('Cards and Corners Iframes Updated Successfully')
