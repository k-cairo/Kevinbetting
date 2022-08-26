from django.core.management.base import BaseCommand
from utils.selenium_functions import open_browser


class Command(BaseCommand):
    help = "Testing if Selenium is working on pythonanywhere."

    def handle(self, *args, **options):
        driver = open_browser()

        driver.get("https://www.google.com")
        print("Page title was '{}'".format(driver.title))

        self.stdout.write('Selenium is working !!! 😊😊😊')
