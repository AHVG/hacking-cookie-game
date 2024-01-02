
from selenium.webdriver.common.by import By

from product import Product
from element_finder import ElementFinder


class Player:

    # TODO: arrumar para pegar o cookie uma vez
    # TODO: arrumar para prefixo dos valores do cookies, por exemplo, million e etc
    # TODO: pegar uma vez todos os produtos disponiveis e atualizar o produto apenas na compra, isso vai otimizar muito o for
    # TODO: comprar os upgrades
    # TODO: fazer uma logica do cookies mais eficiente para ser possivel fazer mais clicks por segundo

    def __init__(self, driver):
        self.__driver = driver
        
        self.__big_cookie = None

        self.__products_prefix = "product"
        self.__products_price_prefix = "productPrice"
        self.__products = []


    def set_up(self):
        self.__big_cookie = ElementFinder.find(self.__driver, (By.ID, "bigCookie"), 10)

        for i in range(0, 20):
            self.__products.append(Product(self.__driver, self.__products_prefix + str(i), self.__products_price_prefix + str(i)))


    def update(self):
        self.__big_cookie.click()

        for i in range(0, 20):

            if self.__products[i].get_price() and self.__products[i].get_price() < int(ElementFinder.find(self.__driver, (By.ID, "cookies")).text.split()[0]):
                self.__products[i].buy()
                
                if i != 19 and not self.__products[i + 1].get_price():
                    self.__products[i + 1].update_price()
                
                break