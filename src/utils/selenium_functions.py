from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def open_browser():
    """
    Open a browser with Selenium.
    :return: Selenium Chrome Webdriver
    """
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        return webdriver.Chrome(options=chrome_options)
    except:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        try:
            service = Service(executable_path=ChromeDriverManager().install())
        except:
            service = Service(executable_path="./chromedriver/chromedriver.exe")
        finally:
            return webdriver.Chrome(service=service, options=chrome_options)


def accept_cookie(driver) -> None:
    """
    Accept cookies from the website 'www.matchendirect.fr'.
    :param driver: Selenium Chrome Webdriver
    :return: None
    """
    try:
        driver.implicitly_wait(1)
        frame = driver.find_element(By.XPATH, '//*[@id="appconsent"]/iframe')
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[1]/button/span').click()
        driver.switch_to.default_content()
    except NoSuchElementException:
        pass
