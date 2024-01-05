import os
import allure
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

    @allure.step
    def get(self, url, params=None):
        res = requests.get(url=url, headers=self.headers, params=params)
        make_attachment(res.text, 'response')
        return res

    @allure.step
    def post(self, url, data):
        res = requests.post(url=url, headers=self.headers, json=data)
        make_attachment(res.text, 'response')
        return res

    @allure.step
    def update(self, url, data=None):
        res = requests.patch(url=url, headers=self.headers, json=data)
        make_attachment(res.text, 'response')
        return res

    @allure.step
    def put(self, url, data=None):
        res = requests.put(url=url, headers=self.headers, json=data)
        make_attachment(res.text, 'response')
        return res

    @allure.step
    def delete(self, url):
        res = requests.delete(url=url, headers=self.headers)
        make_attachment(res.text, 'response')
        return res
