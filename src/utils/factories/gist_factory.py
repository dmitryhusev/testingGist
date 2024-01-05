from src.utils import data_models
from src.utils.request_builder import RequestBuilder
import requests


class RequestGistFactory:
    url = 'https://api.github.com/gists'

    @classmethod
    def get_all_gists(cls, params: dict | None=None):
        res = RequestBuilder().get(cls.url, params=params)
        assert res.status_code == 200
        return [i['id'] for i in res.json()]

    @classmethod
    def post_gist(cls) -> data_models.Gist:
        data = '{"description":"Example of a gist","public":true,"files":{"test2.txt":{"content":"Hello World"}}}'
        res = RequestBuilder().post(cls.url, data)
        assert res.status_code == 201, f'Gist is not created, status code is {res.status_code}'
        validated = validate_gist_creation(res)
        return validated

    @classmethod
    def update_gist(cls, gist_id: str) -> data_models.Gist:
        data = '{"description":"An updated gist description","files":{"README.md":{"content":"Hello World from GitHub"}}}'
        res =  RequestBuilder().update(url=f'{cls.url}/{gist_id}', data=data)
        assert res.status_code == 200, f'Gist is not created, status code is {res.status_code}'
        validated = validate_gist_creation(res)
        return validated

    @classmethod
    def delete_gist(cls, gist_id):
        res = RequestBuilder().delete(url=f'{cls.url}/{gist_id}')
        assert res.status_code == 204


def validate_gist_creation(response: requests.Response) -> data_models.Gist:
    validated = data_models.Gist(
        id_=response.json().get('id'),
        url=response.json().get('url'),
        file_name=response.json().get('files')
    )
    return validated
