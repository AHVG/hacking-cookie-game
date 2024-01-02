
from selenium.webdriver.common.by import By

from utils import find_element


class Product:

    def __init__(self, driver, element_id, price_id):
        self.__driver = driver

        self.__element_id = element_id
        self.__price_id = price_id

        self.__element = find_element(self.__driver, (By.ID, element_id), 10)
        self.__price = None
        self.update_price()


    def get_element(self):
        return self.__element
    

    def get_price(self):
        return self.__price
    
    
    def get_element_id(self):
        return self.__element_id
    

    def get_price_id(self):
        return self.__price_id
    

    def update_price(self):
        self.__price = find_element(self.__driver, (By.ID, self.__price_id)).text.replace(",", "")

        if self.__price:
            self.__price = int(self.__price)

    
    def buy(self):
        self.__element.click()
        self.update_price()
