from src.utils.factories.gist_factory import RequestGistFactory
from typing import List


def create_several_gists(amount: int) -> List:
    gists = []
    for i in range(amount):
        res = RequestGistFactory.post_gist()
        gists.append(res.id_)
    return gists

def delete_all_gists():
    res = RequestGistFactory.get_all_gists()
    ids = [i['id'] for i in res.json()]
    if len(ids) > 0:
        for id_ in ids:
            res = RequestGistFactory.delete_gist(id_)
