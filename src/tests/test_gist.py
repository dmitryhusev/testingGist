from src.utils.factories.gist_factory import RequestGistFactory


def test_delete_all_gists(create_gist):
    res = RequestGistFactory.get_all_gists()
    ids = [i['id'] for i in res.json()]
    if len(ids) > 0:
        for id_ in ids:
            res = RequestGistFactory.delete_gist(id_)
            assert res.status_code == 204