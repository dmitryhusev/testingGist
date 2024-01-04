import os

import requests


class RequestBuilder:
    def __init__(self):
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def get(self, url):
        return requests.get(url=url, headers=self.headers)

    def post(self, url, data):
        return requests.post(url=url, headers=self.headers, data=data)

    def update(self, url, data):
        return requests.patch(url=url, headers=self.headers, data=data)

    def delete(self, url):
        return requests.delete(url=url, headers=self.headers)
