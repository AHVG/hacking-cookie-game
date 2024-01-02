
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(driver, infos, timeout=5):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(infos))


def find_element(driver, infos, timeout=5):
    wait_element(driver, infos, timeout)
    return driver.find_element(*infos)
