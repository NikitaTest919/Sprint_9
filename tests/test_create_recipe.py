import allure
from tests_data.data import RECIPE
from pathlib import Path

class TestCreateRecipe:
    @allure.title("Создание рецепта с загрузкой изображения")
    def test_create_recipe(self, signin_page, create_recipe_page, test_user, recipe):
        # авторизация
        signin_page.open("/")
        signin_page.go_to_signin()
        signin_page.login(test_user["email"], test_user["password"])
        assert signin_page.is_logged_in()

        # создание рецепта
        create_recipe_page.go_to_create()
        create_recipe_page.fill_recipe(recipe["title"], recipe["description"], recipe["cooking_time"], "соль")
        # загрузка файла из assets через pathlib
        create_recipe_page.upload_image(recipe["image"])
        create_recipe_page.submit()

        assert create_recipe_page.is_recipe_present(recipe["title"])
