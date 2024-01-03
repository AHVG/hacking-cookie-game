
from time import time

from selenium.webdriver.common.by import By

from product import Product
from utils import find_element, convert_literal_to_int


class Player:

    def __init__(self, driver):
        self.__driver = driver
        
        self.__big_cookie = None
        self.__cookies = 0
        self.__seconds = 3
        self.__last_update = time()

        self.__products = []


    def set_up(self):
        self.__big_cookie = find_element(self.__driver, (By.ID, "bigCookie"), 10)

        for i in range(0, 20):
            self.__products.append(Product(self.__driver, i))


    def is_time_buy(self):
        current_time = time()

        if current_time - self.__last_update > self.__seconds:
            self.__cookies = convert_literal_to_int(" ".join(find_element(self.__driver, (By.ID, "cookies")).text.split()[:2]))
            self.__last_update = current_time
            return True
        
        return False


    def update(self):
        self.__big_cookie.click()

        if not self.is_time_buy():
            return
        
        try:
            upgrade = find_element(self.__driver, (By.CSS_SELECTOR, "#upgrades .enabled"), 0.05)
            upgrade.click()
        except:
            pass

        for product in self.__products[::-1]:

            if product.get_price() and product.get_price() < self.__cookies:
                
                while product.get_price() < self.__cookies:
                    product.buy()
                    self.__cookies -= product.get_price()
                
                if product.get_id() != 19 and not self.__products[product.get_id() + 1].get_price():
                    self.__products[product.get_id() + 1].update_price()
                
                break