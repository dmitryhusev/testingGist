from src.utils.factories.gist_factory import RequestGistFactory
import datetime

from src.utils.helpers import create_several_gists


def test_gists_for_authenticated_user(create_gists):
    gists = create_gists(2)
    res = RequestGistFactory.get_all_gists()
    for gist in gists:
        assert gist in res


def test_gists_per_page(cleanup_gist):
    gists = create_several_gists(35)
    cleanup_gist(*gists)
    params = {'per_page': 35}
    res = RequestGistFactory.get_all_gists(params)
    assert len(res) >= 35


def test_gists_page(cleanup_gist):
    gists = create_several_gists(35)
    cleanup_gist(*gists)
    params = {'page': 2}
    res = RequestGistFactory.get_all_gists(params)
    assert len(res) >= 5


def test_gists_since(cleanup_gist):
    time = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0).isoformat()
    gist = RequestGistFactory.post_gist()
    cleanup_gist(gist.id_)
    params = {'since': time}
    res = RequestGistFactory.get_all_gists(params)
    assert len(res) > 0
