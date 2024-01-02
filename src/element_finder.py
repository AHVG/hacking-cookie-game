
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class ElementFinder:

    @staticmethod
    def find(driver, infos):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(infos)
        )

        return driver.find_element(*infos)
