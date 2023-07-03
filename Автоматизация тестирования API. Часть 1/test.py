from api.api import Api
import const
import pytest


def test_get_posts():
    response = Api(url=const.URL).get_request(schema=const.get_valid_schema)
    assert response.status_code == 200
    assert response.headers.get('Date') <= const.headers
    print(response.text)


def test_post_posts():
    response = Api(url=const.URL).post_request(body=const.body, schema=const.post_valid_schema)
    assert response.status_code == 201
    assert response.headers.get('Date') <= const.headers
    print(response.text)


def test_delete_posts():
    response = Api(url=const.URL).delete_request()
    assert response.status_code == 200
    assert response.headers.get('Date') <= const.headers
    print(response.text)
