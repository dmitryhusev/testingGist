import datetime
from src.utils.factories.gist_factory import RequestGistFactory, validate_gist
from src.utils.helpers import create_several_gists
from src.utils.request_builder import RequestBuilder


def test_gists_for_authenticated_user(create_gists):
    gists = create_gists(2)
    res = RequestGistFactory.get_all_gists()
    for gist in gists:
        assert gist in res


def test_gists_per_page(cleanup_gist):
    """
    The number of results per page (max 100)
    Default: 30
    """
    gists = create_several_gists(35)
    cleanup_gist(*gists)
    params = {'per_page': 35}
    res = RequestGistFactory.get_all_gists(params=params)
    assert len(res) >= 35


def test_gists_page(cleanup_gist):
    gists = create_several_gists(35)
    cleanup_gist(*gists)
    params = {'page': 2}
    res = RequestGistFactory.get_all_gists(params=params)
    assert len(res) >= 5


def test_gists_since(cleanup_gist):
    time = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0).isoformat()
    gist = RequestGistFactory.post_gist()
    cleanup_gist(gist.id_)
    params = {'since': time}
    res = RequestGistFactory.get_all_gists(params=params)
    assert len(res) > 0


def test_get_gist(create_gist):
    gist = create_gist
    url = f'https://api.github.com/gists/{gist.id_}'
    res = RequestBuilder().get(url)
    assert res.status_code == 200, f'Unable to get gist, current status code is {res.status_code}'
    validate_gist(res)


