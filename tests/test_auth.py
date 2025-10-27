import allure

class TestAuth:
    @allure.title("Авторизация — позитивный сценарий")
    def test_login(self, signin_page, test_user):
        signin_page.open("/")
        signin_page.go_to_signin()
        signin_page.login(test_user["email"], test_user["password"])
        assert signin_page.is_logged_in()
