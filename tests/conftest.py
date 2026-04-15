import allure
import pytest


@pytest.fixture
@allure.step('Подготовка валидных данных')
def get_valid_credentials():
    return 'testatr0207251', '123456'

@pytest.fixture
@allure.step('Подготовка невалидных данных')
def get_invalid_credentials():
    return 'testatr0207251', '123456789'
