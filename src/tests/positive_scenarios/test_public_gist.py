from src.utils.factories.gist_factory import RequestGistFactory


def test_public_gists_default_amount():
    url = 'https://api.github.com/gists/public'
    res = RequestGistFactory.get_all_gists(url=url)
    assert len(res) == 30


def test_public_gists_max_amount():
    url = 'https://api.github.com/gists/public'
    params = {'per_page': 100}
    res = RequestGistFactory.get_all_gists(url=url, params=params)
    assert len(res) == 100


def test_public_gists_pages():
    url = 'https://api.github.com/gists/public'
    params = {'page': 2}
    res = RequestGistFactory.get_all_gists(url=url, params=params)
    assert len(res) == 30
