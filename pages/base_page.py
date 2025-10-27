from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class BasePage:
    def __init__(self, driver, base_url="https://foodgram-frontend-1.prakticum-team.ru"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открыть страницу: {path}")
    def open(self, path="/"):
        self.driver.get(self.base_url + path)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        elem = self.wait.until(EC.element_to_be_clickable((by, locator)))
        elem.click()

    def type(self, by, locator, text):
        elem = self.find(by, locator)
        elem.clear()
        elem.send_keys(text)
