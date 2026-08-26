import json
import requests

from test_api_memes.endpoints.base_endpoint import BaseEndpoint


class AuthorizeEndpoint(BaseEndpoint):
    def check_token(self, token):
        self.response = requests.get(f'{self.URL}/authorize/{token}')
        return self.response

    def read_token(self):
        try:
            with open(self.token_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data["token"]
        except FileNotFoundError:
            return None

    def write_token(self, token):
        with open(self.token_file, "w", encoding="utf-8") as file:
            json.dump({"token", token}, file)

    def authorize(self, body):
        self.response = requests.post(f'{self.URL}/authorize', json=body)
        return self.response.json()['token']

    def get_token(self):
        token = self.read_token()
        if token:
            response = self.check_token(token)
            if response.status_code == 200:
                return response.json()['token']
        new_token = self.authorize({"name": "Murat"})
        self.write_token(new_token)
        return new_token

