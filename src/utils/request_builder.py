import os

import requests

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
        return requests.get(url=url, headers=self.headers, params=params)

    def post(self, url, data):
        return requests.post(url=url, headers=self.headers, json=data)

    def update(self, url, data):
        return requests.patch(url=url, headers=self.headers, data=data)

    def delete(self, url):
        return requests.delete(url=url, headers=self.headers)
