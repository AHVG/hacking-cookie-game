
from time import time

from selenium.webdriver.common.by import By

from product import Product
from utils import find_element


class Player:

    # TODO: arrumar para prefixo dos valores do cookies, por exemplo, million e etc
    # TODO: comprar os upgrades

    def __init__(self, driver):
        self.__driver = driver
        
        self.__big_cookie = None
        self.__cookies = 0
        self.__seconds = 5
        self.__last_update = time()

        self.__products_prefix = "product"
        self.__products_price_prefix = "productPrice"
        self.__products = []


    def set_up(self):
        self.__big_cookie = find_element(self.__driver, (By.ID, "bigCookie"), 10)

        for i in range(0, 20):
            self.__products.append(Product(self.__driver, self.__products_prefix + str(i), self.__products_price_prefix + str(i)))


    def update(self):
        self.__big_cookie.click()

        current_time = time()

        if current_time - self.__last_update > self.__seconds:
            self.__cookies = int(find_element(self.__driver, (By.ID, "cookies")).text.split()[0])
            self.__last_update = current_time
        
        for i in range(0, 20):

            if self.__products[i].get_price() and self.__products[i].get_price() < self.__cookies:
                self.__products[i].buy()
                self.__cookies -= self.__products[i].get_price()
                
                if i != 19 and not self.__products[i + 1].get_price():
                    self.__products[i + 1].update_price()
                
                break