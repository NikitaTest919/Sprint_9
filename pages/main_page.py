from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    LOGOUT_BTN = (By.XPATH, "//button[contains(., 'Выход') or contains(., 'Logout')]")
