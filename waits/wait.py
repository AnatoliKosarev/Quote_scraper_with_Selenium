from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Wait:
    def __init__(self, browser):
        self.browser = browser

    def until_element_is_present(self, element):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element)))
