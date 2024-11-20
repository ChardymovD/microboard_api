import requests
from base.logger import Logger

"""Список базовых HTTP методов"""
class Http_method():
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    token = ""

    @classmethod
    def set_token(cls, token_value):
        cls.token = token_value
        cls.headers['Authorization'] = f"Bearer {cls.token}"

    @classmethod
    def get_headers(cls, use_auth = True):
        if not use_auth:
            temp_headers = cls.headers.copy()
            temp_headers.pop('Authorization', None)
            return temp_headers
        return cls.headers

    @staticmethod
    def get(url, use_auth = True):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body, use_auth = True):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def patch(url, body, use_auth = True):
        Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json=body, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, use_auth = True):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        Logger.add_response(result)
        return result

