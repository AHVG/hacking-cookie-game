
from selenium.webdriver.common.by import By

from element_finder import ElementFinder


class Player:

    def __init__(self, driver) -> None:
        self.__driver = driver

    def update(self):
        cookie = ElementFinder.find(self.__driver, (By.ID, "bigCookie"), 10)
        cookie.click()

        products_prefix = "product"
        products_price_prefix = "productPrice"

        # Talvez chamar so depois de alguns segundos para não ficar consumindo processamento

        for i in range(0, 19):
            cookies = int(ElementFinder.find(self.__driver, (By.ID, "cookies")).text.split()[0])
            product_price = ElementFinder.find(self.__driver, (By.ID, products_price_prefix + str(i)))
            
            if not product_price.text:
                break
            
            if int(product_price.text.replace(",", "")) < cookies:
                ElementFinder.find(self.__driver, (By.ID, products_prefix + str(i))).click()
                break