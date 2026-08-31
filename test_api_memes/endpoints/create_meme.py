from wsgiref import headers

import allure
import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint


class CreateMeme(BaseEndpoint):

    @allure.step("Создать мем")
    def create_meme(self, body, token=None):
        self.response = requests.post(
            f"{self.URL}/meme",
            json=body,
            headers=self.get_headers(token)
        )

        self.get_json()
        return self.response
