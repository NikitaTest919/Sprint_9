from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class SigninPage(BasePage):
    LOGIN_BTN = (By.XPATH, "//a[contains(., 'Войти') or contains(., 'Sign in')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BTN = (By.XPATH, "//button[contains(., 'Войти') or contains(., 'Sign in')]")
    LOGOUT_BTN = (By.XPATH, "//button[contains(., 'Выход') or contains(., 'Logout')]")
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(., 'Создать рецепт') or contains(., 'Create recipe')]")

    @allure.step("Перейти к авторизации")
    def go_to_signin(self):
        self.click(*self.LOGIN_BTN)

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.type(*self.EMAIL_INPUT, text=email)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.SUBMIT_BTN)

    def is_logged_in(self):
        return bool(self.wait.until(lambda d: d.find_element(*self.LOGOUT_BTN)))
