import allure
import requests
import os


class BaseEndpoint:
    base_path = os.path.dirname(__file__)
    project_dir = os.path.dirname(base_path)
    token_file = os.path.join(project_dir, 'token.json')

    URL = 'http://memesapi.course.qa-practice.com/'

    response = None
    json_response = None
    headers = None

    @allure.step("Получить JSON ответа")
    def get_json(self):
        try:
            self.json_response = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json_response = None

    @allure.step("Проверить статус-код {status_code}")
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code, (f'Ожидаемый статус кода {status_code}, '
                                                          f'получен {self.response.status_code}')

    @allure.step("Проверить данные ответа")
    def check_json(self, data):
        for key, value in data.items():
            assert self.json_response[key] == value, (
                f"Поле '{key}' не совпало. "
                f"Ожидали: {value}, "
                f"получили: {self.json_response[key]}"
            )

    def get_headers(self, token=None):
        if token:
            return {"Authorization": token}
        return {}
