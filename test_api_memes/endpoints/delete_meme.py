import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    def delete_meme(self, meme_id):
        self.response = requests.delete(f'{self.URL}/meme/{meme_id}', headers=self.headers)
        return self.response
