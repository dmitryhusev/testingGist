import requests

from src.utils import data_models
from src.utils.request_builder import RequestBuilder


class RequestGistFactory:
    default_url = 'https://api.github.com/gists'

    @classmethod
    def get_all_gists(cls, url: str = None, params: dict | None = None):
        url = url if url else cls.default_url
        res = RequestBuilder().get(url, params=params)
        assert res.status_code == 200, f'Current status code is {res.status_code}'
        return [i['id'] for i in res.json()]

    @classmethod
    def post_gist(cls, body: dict | None = None) -> data_models.Gist:
        payload = {
            "description": "Example of a gist",
            "public": True,
            "files":
                {
                    "test.py":
                        {
                            "content": "print(Hello World)"
                        }
                }
        }
        body = body if body else payload
        res = RequestBuilder().post(cls.default_url, body)
        assert res.status_code == 201, f'Gist is not created, status code is {res.status_code}'
        validated = validate_gist(res)
        return validated

    @classmethod
    def update_gist(cls, gist_id: str, payload: dict) -> data_models.Gist:
        res = RequestBuilder().update(url=f'{cls.default_url}/{gist_id}', data=payload)
        assert res.status_code == 200, f'Gist is not created, status code is {res.status_code}'
        validated = validate_gist(res)
        return validated

    @classmethod
    def delete_gist(cls, gist_id):
        res = RequestBuilder().delete(url=f'{cls.default_url}/{gist_id}')
        assert res.status_code == 204


def validate_gist(response: requests.Response) -> data_models.Gist:
    validated = data_models.Gist(
        id_=response.json().get('id'),
        url=response.json().get('url'),
        file_name=response.json().get('files'),
        description=response.json().get('description')
    )
    return validated
