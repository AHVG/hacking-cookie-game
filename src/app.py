
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as GoogleService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils import find_element
from player import Player


class App:

    def __init__(self):
    
        try:
            self.__service = GoogleService(ChromeDriverManager().install())
            self.__driver = webdriver.Chrome(service=self.__service)
        except:
            self.__service = FirefoxService(GeckoDriverManager().install())
            self.__driver = webdriver.Firefox()

        self.__cookie_game_url = "https://orteil.dashnet.org/cookieclicker/"

    
    def is_running(self):
        return self.__running


    def run(self):
        self.__driver.get(self.__cookie_game_url)
        # self.__driver.fullscreen_window()

        time.sleep(5)

        language = find_element(self.__driver, (By.ID, "langSelect-EN"), 10)
        language.click()

        time.sleep(5)

        player = Player(self.__driver)
        player.set_up()

        while True:
            try:
                player.update()
            except Exception as e:
                print(e)
                break

        self.__driver.quit()