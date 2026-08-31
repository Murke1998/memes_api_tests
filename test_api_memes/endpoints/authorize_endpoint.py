import json

import allure
import requests

from test_api_memes.endpoints.base_endpoint import BaseEndpoint


class AuthorizeEndpoint(BaseEndpoint):
    @allure.step("Проверить валидность токена")
    def check_token(self, token):
        self.response = requests.get(f'{self.URL}/authorize/{token}')
        return self.response

    @allure.step("Прочитать сохранённый токен")
    def read_token(self):
        try:
            with open(self.token_file, "r", encoding="utf-8") as file:
                print('open file')
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    @allure.step("Сохранить новый токен")
    def write_token(self, token):
        with open(self.token_file, "w", encoding="utf-8") as file:
            json.dump({"token": token}, file)

    @allure.step("Авторизоваться и получить новый токен")
    def authorize(self, body):
        self.response = requests.post(f'{self.URL}/authorize', json=body)
        return self.response.json()['token']

    @allure.step("Получить валидный токен")
    def get_token(self):
        token_json = self.read_token()
        if token_json:
            token = token_json['token']
            response = self.check_token(token)
            if response.status_code == 200:
                return token
        new_token = self.authorize({"name": "Murat"})
        print(new_token)
        self.write_token(new_token)
        return new_token
