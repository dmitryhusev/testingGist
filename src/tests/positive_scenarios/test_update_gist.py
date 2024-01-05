from src.utils.factories.gist_factory import RequestGistFactory
from faker import Faker

def test_update_gist(create_gist):
    gist = create_gist
    new_description = Faker().slug()
    payload = {"description": new_description}
    res = RequestGistFactory.update_gist(gist.id_, payload)
    assert res.description == new_description
    assert gist.description != new_description