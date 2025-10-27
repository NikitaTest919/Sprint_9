from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from pathlib import Path

class CreateRecipePage(BasePage):
    CREATE_TAB = (By.XPATH, "//a[contains(., 'Создать рецепт') or contains(., 'Create recipe')]")
    TITLE_INPUT = (By.NAME, "title")
    DESCRIPTION_INPUT = (By.NAME, "description")
    INGREDIENT_INPUT = (By.XPATH, "//input[@placeholder='Ингредиент' or @name='ingredient']")
    INGREDIENT_SUGGESTION = (By.XPATH, "//ul//li")  # упрощённо
    COOKING_TIME_INPUT = (By.NAME, "cooking_time")
    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    SUBMIT_BTN = (By.XPATH, "//button[contains(., 'Создать рецепт') or contains(., 'Create recipe')]")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class,'recipe-card') or contains(., 'recipe')]")
    RECIPE_TITLE = (By.XPATH, "//h1 | //h2")  # пример

    @allure.step("Перейти на вкладку 'Создать рецепт'")
    def go_to_create(self):
        self.click(*self.CREATE_TAB)

    @allure.step("Заполнить поля рецепта (без изображения)")
    def fill_recipe(self, title, description, cooking_time, ingredient):
        self.type(*self.TITLE_INPUT, text=title)
        self.type(*self.DESCRIPTION_INPUT, text=description)
        # ввод ингредиента и выбор из списка
        self.type(*self.INGREDIENT_INPUT, text=ingredient)
        self.wait.until(lambda d: d.find_element(*self.INGREDIENT_SUGGESTION)).click()
        self.type(*self.COOKING_TIME_INPUT, text=cooking_time)

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, image_path: Path):
        # image_path — pathlib.Path; send_keys требует str
        file_input = self.find(*self.IMAGE_INPUT)
        file_input.send_keys(str(image_path.resolve()))

    @allure.step("Создать рецепт")
    def submit(self):
        self.click(*self.SUBMIT_BTN)

    def is_recipe_present(self, title):
        # примитивная проверка — ищем карточку и заголовок
        self.wait.until(lambda d: d.find_element(*self.RECIPE_CARD))
        title_elems = self.driver.find_elements(*self.RECIPE_TITLE)
        return any(title in el.text for el in title_elems)
