
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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