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

    @classmethod
    def get_headers(cls, use_auth = True):
        if not use_auth:
            temp_headers = cls.headers.copy()
            temp_headers.pop('Authorization', None)
            return temp_headers
        return cls.headers

    @staticmethod
    def get(url, use_auth = True):
        result = requests.get(url, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        return result

    @staticmethod
    def post(url, body, use_auth = True):
        result = requests.post(url, json=body, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        return result

    @staticmethod
    def patch(url, body, use_auth = True):
        result = requests.patch(url, json=body, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        return result

    @staticmethod
    def delete(url, use_auth = True):
        result = requests.delete(url, headers=Http_method.get_headers(use_auth), cookies=Http_method.cookie)
        return result

