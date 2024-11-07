import json
import re
from requests import Response

"""Методы для проверки ответов"""

class Cheking():

    """Метод для проверки статус кода ответа"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно! Статус код = " + str(status_code))
        else:
            print("Ошибка! Статус код = " + str(response.status_code))


    """Метод для проверки наличия обязательных полей в ответе"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе"""

    @staticmethod
    def check_json_values(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!")

    """Метод для проверки соответствия данных формату UUID"""

    @staticmethod
    def check_string_is_uuid(response: Response, field_name):
        check = response.json()
        check_info = check.get(field_name)
        uuid_regex =  re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
        string_format = bool(uuid_regex.match(check_info))
        if string_format is True:
            print(field_name + " соответствует формату $uuid")
        else:
            print(field_name + " не соответствует формату $uuid")

    """Метод для проверки соответствия данных формату URI"""

    @staticmethod
    def check_string_is_uri(response: Response, field_name):
        check = response.json()
        check_info = check.get(field_name)
        uri_regex = re.compile(r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$")
        string_format = bool(uri_regex.match(check_info))
        if string_format is True:
            print(field_name + " соответствует формату $uri")
        else:
            print(field_name + " не соответствует формату $uri")

