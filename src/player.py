
from selenium.webdriver.common.by import By

from element_finder import ElementFinder


class Player:

    def __init__(self, driver) -> None:
        self.__driver = driver
        self.__cookie = ElementFinder.find(self.__driver, (By.ID, "bigCookie"), 10)

    def update(self):
        self.__cookie.click()

        products_prefix = "product"
        products_price_prefix = "productPrice"
        end = 4

        # Talvez chamar so depois de alguns segundos para não ficar consumindo processamento
        for i in range(0, 4):
            product_price = ElementFinder.find(self.__driver, (By.ID, products_price_prefix + str(i)))

            print(product_price.text)