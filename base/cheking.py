import json
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

