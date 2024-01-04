import pytest
from src.utils import data_models
from src.utils.factories.gist_factory import RequestGistFactory


@pytest.fixture
def create_gist():
    res = RequestGistFactory.post_gist()
    assert res.status_code == 201, f'Gist is not created, status code is {res.status_code}'
    yield data_models.Gist(
        id_=res.json().get('id'),
        url=res.json().get('url'),
        file_name=res.json().get('files')
    )
    RequestGistFactory.delete_gist(res.json().get('id'))

