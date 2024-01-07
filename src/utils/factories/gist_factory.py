import requests
import allure
from src.utils import data_models
from src.utils.request_builder import RequestBuilder
from src.settings import DEFAULT_URL


class RequestGistFactory:

    error_message = 'Invalid request, status code: is %s, message: %s'

    @classmethod
    def get_all_gists(cls, url: str = None, params: dict | None = None):
        url = url if url else DEFAULT_URL
        res = RequestBuilder().get_query(url, params=params)
        assert res.status_code == 200, cls.error_message % (res.status_code, res.text)
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
        res = RequestBuilder().post_query(DEFAULT_URL, body)
        assert res.status_code == 201, cls.error_message % (res.status_code, res.text)
        validated = validate_gist(res)
        return validated

    @classmethod
    def update_gist(cls, gist_id: str, payload: dict) -> data_models.Gist:
        res = RequestBuilder().update_query(url=f'{DEFAULT_URL}/{gist_id}', data=payload)
        assert res.status_code == 200, cls.error_message % (res.status_code, res.text)
        validated = validate_gist(res)
        return validated

    @classmethod
    def delete_gist(cls, gist_id):
        res = RequestBuilder().delete_query(url=f'{DEFAULT_URL}/{gist_id}')
        assert res.status_code == 204, cls.error_message % (res.status_code, res.text)

@allure.step
def validate_gist(response: requests.Response) -> data_models.Gist:
    validated = data_models.Gist(
        id_=response.json().get('id'),
        url=response.json().get('url'),
        file_name=response.json().get('files'),
        description=response.json().get('description')
    )
    return validated
