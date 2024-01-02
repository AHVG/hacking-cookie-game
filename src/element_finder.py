
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Será que só uma módulo com as funções não é o suficiente? 
# Gosto da ideia de um "namespace" para esse tipo de função

class ElementFinder:

    @staticmethod
    def wait_element(driver, infos, timeout=5):
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(infos))

    @staticmethod
    def find(driver, infos, timeout=5):
        ElementFinder.wait_element(driver, infos, timeout)
        return driver.find_element(*infos)
