import allure
import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):

    @allure.step("Удалить мем с id={meme_id}")
    def delete_meme(self, meme_id, token):
        self.response = requests.delete(f'{self.URL}/meme/{meme_id}', headers=self.get_headers(token))
        return self.response
