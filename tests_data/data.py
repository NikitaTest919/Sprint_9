from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TEST_USER = {
    "username": "autotest_user",
    "email": "autotest_user@example.com",
    "password": "StrongP@ssw0rd"
}

RECIPE = {
    "title": "Автотестовый рецепт",
    "description": "Описание рецепта для автотеста",
    "cooking_time": "10",
    "image": BASE_DIR / "assets" / "test_image.jpg"
}
