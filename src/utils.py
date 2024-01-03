import traceback

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as GoogleService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def load_driver():
    driver = None
    service = None

    try:
        service = GoogleService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        traceback.print_exc()
        print(e)
        print("Possivelmente você não tem o chrome. Se for o caso, baixe-o e tente novamente.")
    
    if not driver:
        try:
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        except Exception as e:
            traceback.print_exc()
            print(e)
            print("Possivelmente você não tem o Firefox. Se for o caso, baixe-o e tente novamente.")
            return None, None

    return driver, service


def wait_element(driver, infos, timeout=5):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(infos))


def find_element(driver, infos, timeout=5):
    wait_element(driver, infos, timeout)
    return driver.find_element(*infos)


def convert_literal_to_int(value_text):
    multipliers = {'million': 1_000, 'billion': 1_000_000} # Não sei se tem mais, possivelmente tem

    parts = value_text.replace(",", "").split()

    if len(parts) == 0:
        value = 0
    elif len(parts) == 1:
        value = int(parts[0])
    else:
        value = int(parts[0]) * multipliers.get(parts[1].lower(), 1)    

    return value


