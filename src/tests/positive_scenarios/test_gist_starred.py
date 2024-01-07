from src.utils.request_builder import RequestBuilder
from src.settings import DEFAULT_URL


def test_gist_star(create_gist):
    gist_id = create_gist.id_
    url = f'{DEFAULT_URL}/{gist_id}/star'
    builder = RequestBuilder()
    builder.headers['Content-Length'] = '0'
    res = builder.put_query(url)
    assert res.status_code == 204


def test_gist_unstar(create_gist):
    gist_id = create_gist.id_
    url = f'{DEFAULT_URL}/{gist_id}/star'
    builder = RequestBuilder()
    builder.headers['Content-Length'] = '0'
    res = builder.put_query(url)
    assert res.status_code == 204
    res = builder.delete_query(url)
    assert res.status_code == 204

