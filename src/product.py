
from selenium.webdriver.common.by import By

from utils import find_element, convert_literal_to_int


class Product:

    products_prefix = "product"
    products_price_prefix = "productPrice"

    def __init__(self, driver, id):
        self.__driver = driver

        self.__element_id = Product.products_prefix + str(id)
        self.__price_id = Product.products_price_prefix + str(id)

        self.__element = find_element(self.__driver, (By.ID, self.__element_id), 10)
        self.__price = 0
        self.update_price()

        self.__id = id


    def get_element(self):
        return self.__element
    

    def get_price(self):
        return self.__price
    
    
    def get_element_id(self):
        return self.__element_id
    

    def get_price_id(self):
        return self.__price_id
    

    def get_id(self):
        return self.__id


    def update_price(self):
        self.__price = convert_literal_to_int(find_element(self.__driver, (By.ID, self.__price_id)).text.replace(",", ""))

    
    def buy(self):
        self.__element.click()
        self.update_price()
