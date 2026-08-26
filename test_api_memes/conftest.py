import pytest

from test_api_memes.endpoints.create_meme import CreateMeme
from test_api_memes.endpoints.authorize_endpoint import AuthorizeEndpoint
from test_api_memes.endpoints.delete_meme import DeleteMeme
from test_api_memes.endpoints.get_meme import GetMeme
from test_api_memes.endpoints.update_meme import UpdateMeme

@pytest.fixture(scope='session')
def token():
    return AuthorizeEndpoint().get_token()

@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()

@pytest.fixture()
def authorize_meme_endpoint():
    return AuthorizeEndpoint()

@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()

@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()

@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()



