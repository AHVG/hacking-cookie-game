
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from element_finder import ElementFinder


class App:

    def __init__(self) -> None:
        self.__service = Service(ChromeDriverManager().install())
        self.__options = webdriver.ChromeOptions()
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__browser = None
        self.__running = True
        self.__cookie_game_url = "https://orteil.dashnet.org/cookieclicker/"

        try:
            self.__browser = webdriver.Chrome(service = self.__service, options=self.__options)
        except:
            self.__browser = webdriver.Firefox()

    
    def is_running(self):
        return self.__running


    def run(self) -> None:
        self.__browser.get(self.__cookie_game_url)

        language = ElementFinder.find(self.__browser, (By.ID, "langSelect-EN"))
        language.click()

        while self.is_running():
            pass

        self.__browser.close()
        self.__browser.quit()