
from selenium.webdriver.common.by import By

from element_finder import ElementFinder


class Player:

    def __init__(self, driver) -> None:
        self.__driver = driver
        self.__cookie = ElementFinder.find(self.__driver, (By.ID, "bigCookie"))

    def update(self):
        self.__cookie.click()