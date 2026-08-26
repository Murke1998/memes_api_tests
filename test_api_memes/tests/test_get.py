import pytest


@pytest.mark.parametrize("body",[{'text': 'test',
                               'url': 'string',
                               'tags': [],
                               'info': {}}])
def test_create_meme(body, create_meme_endpoint, token, get_meme_endpoint, update_meme_endpoint, delete_meme_endpoint):
    create_meme_endpoint.create_meme(body = body, headers=token)
    create_meme_endpoint.check_status_code(200)
    create_meme_endpoint.check_json(body)


