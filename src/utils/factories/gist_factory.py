from src.utils.request_builder import RequestBuilder


class RequestGistFactory:
    url = 'https://api.github.com/gists'

    @classmethod
    def get_all_gists(cls):
        return RequestBuilder().get(cls.url)

    @classmethod
    def post_gist(cls):
        data = '{"description":"Example of a gist","public":true,"files":{"test2.txt":{"content":"Hello World"}}}'
        return RequestBuilder().post(cls.url, data)

    @classmethod
    def update_gist(cls, gist_id):
        data = '{"description":"An updated gist description","files":{"README.md":{"content":"Hello World from GitHub"}}}'
        return RequestBuilder().update(url=f'{cls.url}/{gist_id}', data=data)

    @classmethod
    def delete_gist(cls, gist_id):
        return RequestBuilder().delete(url=f'{cls.url}/{gist_id}')
