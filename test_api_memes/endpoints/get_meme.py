import allure
import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint):

    @allure.step("Получить список всех мемов")
    def get_memes(self, token=None):
        self.response = requests.get(f'{self.URL}/meme', headers=self.get_headers(token))
        self.get_json()
        return self.response

    @allure.step("Получить мем с id={meme_id}")
    def get_meme(self, meme_id, token=None):
        self.response = requests.get(f'{self.URL}/meme/{meme_id}', headers=self.get_headers(token))
        self.get_json()
        return self.response
