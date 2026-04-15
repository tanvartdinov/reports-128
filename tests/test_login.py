# pip install pytest-html
# python -m pytest -v --tb=short --html=report.html
# pip install allure-pytest
# pip install allure-python-commons
# python3 -m pytest -v --tb=short --alluredir=allure-results
# allure serve allure-results

import requests
import allure

from utils.api_client import APIClient
from utils.helpers import assert_status_code


@allure.epic('Авторизация')
@allure.feature('Проверка авторизации запросом')
class TestLoginAPI:
    @allure.title('Успешная авторизация для старых приставок')
    @allure.description('Авторизация по методу /login с валидным паролем возвращает ответ 200')
    def test_login_success(self, get_valid_credentials):
        login, password = get_valid_credentials
        client = APIClient()
        response = client.login(login, password)
        assert_status_code(response, 200)

    @allure.title('Неуспешная авторизация для старых приставок')
    @allure.description('Авторизация по методу /login с невалидным паролем возвращает ответ 403')
    def test_login_failed_invalid_password(self, get_invalid_credentials):
        login, password = get_invalid_credentials
        client = APIClient()
        response = client.login(login, password)
        assert_status_code(response, 404)

    @allure.title('Успешная авторизация для новых приставок')
    @allure.description('Авторизация по методу /v2/login с валидным паролем возвращает ответ 200')
    def test_login_v2_success(self, get_valid_credentials):
        login, password = get_valid_credentials
        client = APIClient()
        response = client.login_v2(login, password)
        assert_status_code(response, 200)

    @allure.title('Неуспешная авторизация для новых приставок')
    @allure.description('Авторизация по методу /v2/login с невалидным паролем возвращает ответ 403')
    def test_login_v2_failed_invalid_password(self, get_invalid_credentials):
        login, password = get_invalid_credentials
        client = APIClient()
        response = client.login_v2(login, password)
        assert_status_code(response, 403)
