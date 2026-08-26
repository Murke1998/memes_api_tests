import requests
import os

class BaseEndpoint:

    base_path = os.path.dirname(__file__)
    project_dir = os.path.dirname(base_path)
    token_file = os.path.join(project_dir, 'token.json')
    URL = 'http://memesapi.course.qa-practice.com/'
    headers = {'Authorization': 'BoHdNENJxcVxxV7'}
    json = {'name': 'Murat'}
    response = None


    # Получает Жсон из ответа
    def get_json(self):
        try:
            self.json_response = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json_response = None

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code, (f'Ожидаемый статус кода {status_code}, '
                                                          f'получен {self.response.status_code}')

    def check_json(self, data):
        for key, value in data.items():
            assert self.json_response[key] == value



