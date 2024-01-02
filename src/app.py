import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from element_finder import ElementFinder
from player import Player


class App:

    def __init__(self) -> None:
        self.__service = Service(ChromeDriverManager().install())
        self.__options = webdriver.ChromeOptions()
        self.__options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__driver = None
        self.__running = True
        self.__cookie_game_url = "https://orteil.dashnet.org/cookieclicker/"

        try:
            self.__driver = webdriver.Chrome(service = self.__service, options=self.__options)
        except:
            self.__driver = webdriver.Firefox()

    
    def is_running(self):
        return self.__running


    def run(self) -> None:
        self.__driver.get(self.__cookie_game_url)

        language = ElementFinder.find(self.__driver, (By.ID, "langSelect-EN"), 10)
        language.click()

        player = Player(self.__driver)

        while self.is_running():
            player.update()

        self.__driver.close()
        self.__driver.quit()