
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
        self.__seconds = 3
        self.__last_update = time()

        self.__products_prefix = "product"
        self.__products_price_prefix = "productPrice"
        self.__products = []


    def set_up(self):
        self.__big_cookie = find_element(self.__driver, (By.ID, "bigCookie"), 10)

        for i in range(0, 20):
            self.__products.append(Product(self.__driver, self.__products_prefix + str(i), self.__products_price_prefix + str(i), i))


    def is_time_buy(self):
        current_time = time()

        if current_time - self.__last_update > self.__seconds:
            self.__cookies = int(find_element(self.__driver, (By.ID, "cookies")).text.split()[0].replace(",", ""))
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

        # Ordenar pelo mais caro
        products = sorted(self.__products, key=lambda x: x.get_price(), reverse=True)
        for product in products:

            if product.get_price() and product.get_price() < self.__cookies:
                
                while product.get_price() < self.__cookies:
                    product.buy()
                    self.__cookies -= product.get_price()
                
                if product.get_number() != 19 and not self.__products[product.get_number() + 1].get_price():
                    self.__products[product.get_number() + 1].update_price()
                
                break