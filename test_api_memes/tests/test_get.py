import pytest


# Создание → получение
def test_create_meme(new_meme,
                     get_meme_endpoint,
                     token):
    meme_id, body = new_meme

    get_meme_endpoint.get_meme(meme_id, token)
    get_meme_endpoint.check_status_code(200)
    get_meme_endpoint.check_json(body)


# Создание → изменение → проверка


def test_meme_changes_are_saved(
        new_meme,
        token,
        get_meme_endpoint,
        update_meme_endpoint
):
    meme_id, body = new_meme

    updated_body = {
        "id": meme_id,
        "text": "updated text",
        "url": "updated url",
        "tags": ["updated"],
        "info": {"test": ["updated"]}
    }

    update_meme_endpoint.update_meme(
        meme_id,
        body=updated_body,
        token=token
    )
    update_meme_endpoint.check_status_code(200)

    get_meme_endpoint.get_meme(meme_id, token)
    get_meme_endpoint.check_status_code(200)

    expected_data = {
        "text": updated_body["text"],
        "url": updated_body["url"],
        "tags": updated_body["tags"],
        "info": updated_body["info"]
    }

    get_meme_endpoint.check_json(expected_data)


# Создание → удаление → проверка

def test_deleted_meme_cannot_be_received(
        new_meme,
        token,
        get_meme_endpoint,
        delete_meme_endpoint
):
    meme_id, body = new_meme

    delete_meme_endpoint.delete_meme(meme_id, token)
    delete_meme_endpoint.check_status_code(200)

    get_meme_endpoint.get_meme(meme_id, token)
    get_meme_endpoint.check_status_code(404)


# Несуществующий id
def test_no_meme(get_meme_endpoint, token):
    get_meme_endpoint.get_meme(999999999999, token)
    get_meme_endpoint.check_status_code(404)


# Без авторизации

@pytest.mark.parametrize("body", [{'text': 'Qa test',
                                   'url': 'My home my home',
                                   'tags': ['Me', 'wife'],
                                   'info': {'grand': ['grandM', 'grandF']}}])
def test_authorization(create_meme_endpoint, body):
    create_meme_endpoint.create_meme(body=body)
    create_meme_endpoint.check_status_code(401)
