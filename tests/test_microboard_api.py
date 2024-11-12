from django.db.models.expressions import result
from requests import Response
from base.cheking import Cheking
from base.api import Microboard_board_api


class Test_Board_api():

    """Инициализация атрибутов"""
    def __init__(self):
        self.boardId = None
        self.newBoardId = None


    """Создание новой доски"""
    def test_create_a_board(self):
        print("Метод POST")
        result_post: Response = Microboard_board_api.create_a_board("", "")
        Cheking.check_status_code(result_post, 201)
        Cheking.check_json_token(result_post, ['boardId', 'boardUrl', 'board'])
        Cheking.check_string_is_uuid(result_post, 'boardId')
        Cheking.check_string_is_uri(result_post, 'boardUrl')
        Cheking.check_string_is_uuid(result_post, 'board')

        check_post = result_post.json()
        self.boardId = check_post.get('boardId')

        print("Метод GET")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(self.boardId)
        Cheking.check_status_code(result_get, 200)

    """Дублирование доски"""
    def test_duplicate_a_board(self):
        print("Метод POST")
        result_post: Response = Microboard_board_api.duplicate_a_board(self.boardId, "")
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['newBoardId'])
        Cheking.check_string_is_uuid(result_post, 'newBoardId')
        assert result_post.json().get('newBoardId') != self.boardId

        check_post = result_post.json()
        self.newBoardId = check_post.get('newBoardId')

        print("Метод Get")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(result_post.json().get(self.newBoardId))
        Cheking.check_status_code(result_get, 200)


    """Переименование доски"""
    def test_rename_a_board(self):
        print("Метод PATCH")
        result_patch: Response = Microboard_board_api.rename_a_board(self.newBoardId, "Example")
        Cheking.check_status_code(result_patch, 200)

        print("Метод GET")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(self.newBoardId)
        Cheking.check_status_code(result_get, 200)


    """Удаление доски"""
    def test_delete_a_board(self):
        print("Метод DELETE")
        result_delete: Response = Microboard_board_api.delete_a_board(self.newBoardId)
        Cheking.check_status_code(result_delete, 204)

        print("Метод Get")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(self.newBoardId)
        Cheking.check_status_code(result_get, 404)




