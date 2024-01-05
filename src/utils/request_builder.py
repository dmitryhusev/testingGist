import os

import requests

from src.utils.allure_attach import make_attachment

TOKEN = os.getenv("GITHUB_TOKEN")


class RequestBuilder:
    def __init__(self, token=None):
        self.token = token if token else TOKEN
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def get(self, url, params=None):
        make_attachment(url, 'request url')
        make_attachment(str(params), 'request query params')
        res =  requests.get(url=url, headers=self.headers, params=params)
        make_attachment(res.text, 'response')
        return res

    def post(self, url, data):
        make_attachment(url, 'request url')
        make_attachment(str(data), 'request payload')
        res = requests.post(url=url, headers=self.headers, json=data)
        make_attachment(res.text, 'response')
        return res

    def update(self, url, data=None):
        make_attachment(url, 'request url')
        make_attachment(str(data), 'request payload')
        res = requests.patch(url=url, headers=self.headers, json=data)
        make_attachment(res.text, 'response')
        return res
    def put(self, url, data=None):
        make_attachment(url, 'request url')
        make_attachment(str(data), 'request payload')
        res = requests.put(url=url, headers=self.headers, json=data)
        make_attachment(res.text, 'response')
        return res
    def delete(self, url):
        make_attachment(url, 'request url')
        res = requests.delete(url=url, headers=self.headers)
        make_attachment(res.text, 'response')
        return res