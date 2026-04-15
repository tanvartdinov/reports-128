import allure


@allure.step('Проверка статус-кода ответа сервера')
def assert_status_code(response, expected_status):
    assert response.status_code == expected_status