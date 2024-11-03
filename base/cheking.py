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
