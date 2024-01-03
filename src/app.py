
import traceback
import time
import sys

from selenium.webdriver.common.by import By

from utils import find_element, load_driver
from player import Player


class App:

    def __init__(self):
        self.__driver = None
        self.__service = None

        self.__driver, self.__service = load_driver()

        if not self.__driver:
            print("Possivelmente ocorreu algum problema nos drivers. Tente baixar ou o Chrome ou o Firefox. Preferencialmente o Chrome.")
            sys.exit(1)

        self.__cookie_game_url = "https://orteil.dashnet.org/cookieclicker/"

    
    def is_running(self):
        return self.__running


    def run(self):
        self.__driver.get(self.__cookie_game_url)
        self.__driver.fullscreen_window()

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
                traceback.print_exc()
                print(e)
                break

        self.__driver.quit()