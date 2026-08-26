import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint

class GetMeme(BaseEndpoint):
    def get_memes(self):
        self.response = requests.get(f'{self.URL}/meme',headers=self.headers)
        return self.response

    def get_meme(self, meme_id):
        self.response = requests.get(f'{self.URL}/meme/{meme_id}', headers=self.headers)
        return self.response


