import allure
from tests_data.data import BASE_DIR
import pytest

class TestSignup:
    @allure.title("Создание аккаунта — позитивный сценарий")
    def test_create_account(self, signup_page, test_user):
        signup_page.open("/")
        signup_page.go_to_signup()
        signup_page.register(test_user["username"], test_user["email"], test_user["password"])
        assert signup_page.is_redirected_to_signin()
