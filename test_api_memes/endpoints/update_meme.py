import requests
from test_api_memes.endpoints.base_endpoint import BaseEndpoint

body = {'id': 872,
'text': '456',
'url': 'string',
'tags': [],
'info': {}}

class UpdateMeme(BaseEndpoint):
    def update_meme(self):
        self.response = requests.put(f'{self.URL}/meme/{body["id"]}', json=body, headers=self.headers)
        return self.response