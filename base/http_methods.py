import requests

"""Список базовых HTTP методов"""
class Http_method():
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    token = ""

    @classmethod
    def set_token(cls, token_value):
        cls.token = token_value
        cls.headers['Authorization'] = f"Bearer {cls.token}"

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def patch(url, body):
        result = requests.patch(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

