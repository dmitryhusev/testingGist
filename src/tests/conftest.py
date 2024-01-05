import pytest
from src.utils.factories.gist_factory import RequestGistFactory
from src.utils.helpers import create_several_gists


@pytest.fixture
def create_gist():
    res = RequestGistFactory.post_gist()
    yield res
    RequestGistFactory.delete_gist(res.id_)


@pytest.fixture
def cleanup_gist():
    gist_ids = []

    def wrapper(*gists):
        for gist in gists:
            gist_ids.append(gist)
    yield wrapper
    [RequestGistFactory.delete_gist(id_) for id_ in gist_ids]


@pytest.fixture
def create_gists():
    ids = []

    def wrapper(amount):
        inner_ids = create_several_gists(amount)
        ids.extend(inner_ids)
        return inner_ids
    yield wrapper
    if len(ids) > 0:
        for id_ in ids:
            RequestGistFactory.delete_gist(id_)





