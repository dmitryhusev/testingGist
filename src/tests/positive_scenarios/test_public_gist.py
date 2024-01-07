from src.utils.factories.gist_factory import RequestGistFactory
from src.settings import DEFAULT_URL


def test_public_gists_default_amount():
    url = f'{DEFAULT_URL}/public'
    res = RequestGistFactory.get_all_gists(url=url)
    assert len(res) == 30


def test_public_gists_max_amount():
    url = f'{DEFAULT_URL}/public'
    params = {'per_page': 100}
    res = RequestGistFactory.get_all_gists(url=url, params=params)
    assert len(res) == 100


def test_public_gists_pages():
    url = f'{DEFAULT_URL}/public'
    params = {'page': 2}
    res = RequestGistFactory.get_all_gists(url=url, params=params)
    assert len(res) == 30
