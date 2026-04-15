import allure
import requests


class APIClient:
    base_url = 'https://fe.rc.smotreshka.tv'

    @allure.step('Запрос авторизации')
    def login(self, login, password):
        data = f'email={login}&password={password}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(f'{self.base_url}/login',
                                 headers=headers,
                                 data=data)

        allure.attach(f'{self.base_url}/login', name='URL', attachment_type=allure.attachment_type.TEXT)
        allure.attach(data, name='Payload', attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response', attachment_type=allure.attachment_type.JSON)

        return response

    @allure.step('Запрос авторизации')
    def login_v2(self, login, password):
        data = f'email={login}&password={password}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(f'{self.base_url}/v2/login',
                                 headers=headers,
                                 data=data)

        allure.attach(f'{self.base_url}/login', name='URL', attachment_type=allure.attachment_type.TEXT)
        allure.attach(data, name='Payload', attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response', attachment_type=allure.attachment_type.JSON)

        return response
