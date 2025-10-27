from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class SignupPage(BasePage):
    # локаторы
    CREATE_ACCOUNT_BTN = (By.XPATH, "//a[contains(., 'Создать аккаунт') or contains(., 'Register')]")
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BTN = (By.XPATH, "//button[contains(., 'Создать аккаунт') or contains(., 'Sign up')]")
    SIGNIN_FORM = (By.XPATH, "//form[contains(., 'Войти') or contains(@class,'signin')]")

    @allure.step("Перейти к регистрации")
    def go_to_signup(self):
        self.click(*self.CREATE_ACCOUNT_BTN)

    @allure.step("Заполнить форму регистрации")
    def register(self, username, email, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.EMAIL_INPUT, text=email)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.SUBMIT_BTN)

    def is_redirected_to_signin(self):
        return bool(self.wait.until(lambda d: d.find_element(*self.SIGNIN_FORM)))
