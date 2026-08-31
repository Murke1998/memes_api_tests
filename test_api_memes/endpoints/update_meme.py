import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint

body = {'id': 872,
        'text': '456',
        'url': 'string',
        'tags': [],
        'info': {}}


class UpdateMeme(BaseEndpoint):
    def update_meme(self, id_meme, body, token=None):
        self.response = requests.put(f'{self.URL}/meme/{id_meme}', json=body, headers=self.get_headers(token))
        self.get_json()
        return self.response
