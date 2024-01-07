from faker import Faker
import pytest
from src.utils.factories.gist_factory import RequestGistFactory
from src.utils.request_builder import RequestBuilder
from src.settings import DEFAULT_URL


pytestmark = pytest.mark.negative


def test_gist_invalid_token():
    builder = RequestBuilder(token='invalid_token')
    res = builder.get_query(DEFAULT_URL)
    assert res.status_code == 401


def test_gist_invalid_payload():
    invalid_payload = {'hello': 'world'}
    res = RequestBuilder().post_query(DEFAULT_URL, invalid_payload)
    assert res.status_code == 422


def test_gist_incorrect_page_number(create_gist):
    # The number of results per page (max 100), meaning that page 101 should not exist and res is empty
    params = {'page': 101}
    res = RequestGistFactory.get_all_gists(params=params)
    assert not res


def test_public_gists_max_amount_exceeded():
    url = f'{DEFAULT_URL}/public'
    params = {'page': 101}
    res = RequestBuilder().get_query(url, params=params)
    assert res.status_code == 422


def test_get_not_existing_gist():
    invalid_gist_id = ''
    url = f'{DEFAULT_URL}/{invalid_gist_id}'
    res = RequestBuilder().get_query(url)
    assert res.status_code == 404


def test_update_not_existing_gist():
    invalid_gist_id = ''
    url = f'{DEFAULT_URL}/{invalid_gist_id}'
    new_description = Faker().slug()
    payload = {"description": new_description}
    res = RequestBuilder().update_query(url, data=payload)
    assert res.status_code == 404


def test_delete_not_existing_gist():
    invalid_gist_id = ''
    res = RequestBuilder().delete_query(url=f'{DEFAULT_URL}/{invalid_gist_id}')
    assert res.status_code == 404


def test_gist_not_starred(create_gist):
    gist_id = create_gist.id_
    url = f'https://api.github.com/gists/{gist_id}/star'
    res = RequestBuilder().get_query(url)
    assert res.status_code == 404
