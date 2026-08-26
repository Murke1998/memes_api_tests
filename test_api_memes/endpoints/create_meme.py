from wsgiref import headers

import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint



class CreateMeme(BaseEndpoint):
    def create_meme(self, body, headers):
        self.response = requests.post(f'{self.URL}/meme', json=body, headers = headers)
        self.get_json()
        return self.response
