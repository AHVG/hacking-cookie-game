
from selenium.webdriver.common.by import By

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
        self.__products = [None for _ in range(0, 20)]


    def set_up(self):
        self.__big_cookie = ElementFinder.find(self.__driver, (By.ID, "bigCookie"), 10)

        for i in range(0, 20):
            self.update_product({"price_id": self.__products_price_prefix + str(i),
                                "product_id": self.__products_prefix + str(i),
                                "number": i})


    def update_product(self, product_infos):
        product_price = ElementFinder.find(self.__driver, (By.ID, product_infos["price_id"])).text.replace(",", "")
        
        if product_price:
            product_price = int(product_price)
        
        product = ElementFinder.find(self.__driver, (By.ID, product_infos["product_id"]))

        self.__products[product_infos["number"]] = {"price": product_price, "product": product}


    def update(self):
        self.__big_cookie.click()

        for i in range(0, 20):

            if self.__products[i]["price"] and self.__products[i]["price"] < int(ElementFinder.find(self.__driver, (By.ID, "cookies")).text.split()[0]):
                self.__products[i]["product"].click()
                self.update_product({"price_id": self.__products_price_prefix + str(i),
                                     "product_id": self.__products_prefix + str(i),
                                     "number": i})
                # TODO: Adicionar logica para atualizar os proximos quando se compra o ultimo produto
                break