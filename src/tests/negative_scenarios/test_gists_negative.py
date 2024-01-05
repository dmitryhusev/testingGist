from src.utils.factories.gist_factory import RequestGistFactory
from src.utils.request_builder import RequestBuilder

URL = 'https://api.github.com/gists'


def test_gist_invalid_token():
    builder = RequestBuilder(token='invalid_token')
    res = builder.get(URL)
    assert res.status_code == 401


def test_gist_invalid_payload():
    invalid_payload = {'hello': 'world'}
    res = RequestBuilder().post(URL, invalid_payload)
    assert res.status_code == 422

def test_gist_incorrect_page_number(create_gist):
    # The number of results per page (max 100), meaning that page 101 should not exist and res is empty
    params = {'page': 101}
    res = RequestGistFactory.get_all_gists(params=params)
    assert not res


def test_public_gists_max_amount_exceeded():
    url = 'https://api.github.com/gists/public'
    params = {'page': 101}
    res = RequestBuilder().get(url, params=params)
    assert res.status_code == 422