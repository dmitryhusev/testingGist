from src.utils.request_builder import RequestBuilder


def test_gist_star(create_gist):
    gist_id = create_gist.id_
    url = f'https://api.github.com/gists/{gist_id}/star'
    builder = RequestBuilder()
    builder.headers['Content-Length'] = '0'
    res = builder.put(url)
    assert res.status_code == 204


def test_gist_unstar(create_gist):
    gist_id = create_gist.id_
    url = f'https://api.github.com/gists/{gist_id}/star'
    builder = RequestBuilder()
    builder.headers['Content-Length'] = '0'
    res = builder.put(url)
    assert res.status_code == 204
    res = builder.delete(url)
    assert res.status_code == 204

