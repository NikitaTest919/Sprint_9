import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Импортируем Page Object классы
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.create_recipe_page import CreateRecipePage


# URL Selenoid
SELENOID_URL = os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub")


# Настройки браузера
@pytest.fixture(scope="session")
def browser_options():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
    return options


# Фикстура WebDriver
@pytest.fixture
def driver(browser_options):
    caps = DesiredCapabilities.CHROME.copy()
    caps["browserName"] = "chrome"
    caps["browserVersion"] = "128.0"
    caps["selenoid:options"] = {"enableVNC": False, "enableVideo": False}

    for key, value in caps.items():
        browser_options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=SELENOID_URL,
        options=browser_options
    )

    driver.maximize_window()

    yield driver

    # Прикрепляем скриншот в Allure при завершении
    try:
        if hasattr(driver, "get_screenshot_as_png"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    finally:
        driver.quit()


# ----------- PAGE FIXTURES -----------

@pytest.fixture
def signin_page(driver):
    """Фикстура для страницы авторизации"""
    return SigninPage(driver)


@pytest.fixture
def signup_page(driver):
    """Фикстура для страницы регистрации"""
    return SignupPage(driver)


@pytest.fixture
def create_recipe_page(driver):
    """Фикстура для страницы создания рецепта"""
    return CreateRecipePage(driver)


# ----------- DATA FIXTURES -----------

@pytest.fixture
def test_user():
    """Тестовый пользователь"""
    return {
        "username": "Testing",
        "email": "test_919@yandex.ru",
        "password": "123456789Testov"
    }


@pytest.fixture
def recipe():
    """Тестовые данные для рецепта"""
    return {
        "title": "Тестовый рецепт",
        "description": "Простой тестовый рецепт",
        "ingredients": ["Яйцо", "Молоко", "Мука"],
        "image_path": os.path.join("assets", "test_image.jpg")
    }
