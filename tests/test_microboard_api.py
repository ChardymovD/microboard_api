import pytest
import allure
from requests import Response
from base.cheking import Cheking
from base.api import Microboard_board_api

@pytest.fixture(scope="class")
def board_data():
    data = {}
    response: Response = Microboard_board_api.create_a_board('Test Board', 'root', use_auth=True)
    data['boardId'] = response.json().get('boardId')

    yield data
    if 'boardId' in data:
        Microboard_board_api.delete_a_board(data['boardId'])

@allure.epic("Test Board API")
class Test_Board_api():

    """Создание новой доски"""
    @allure.description("Create a board")
    def test_create_a_board(self):
        print("Метод POST")
        result_post: Response = Microboard_board_api.create_a_board("", "root", use_auth=True)
        Cheking.check_status_code(result_post, 201)
        Cheking.check_json_token(result_post, ['boardId', 'boardUrl', 'board', 'authorKey'])
        Cheking.check_string_is_uuid(result_post, 'boardId')
        Cheking.check_string_is_uri(result_post, 'boardUrl')
        Cheking.check_string_is_uri(result_post, 'board')
        Cheking.check_string_is_uuid(result_post, 'authorKey')

        check_post = result_post.json()
        self.boardId = check_post.get('boardId')

        print("Метод GET")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(self.boardId, use_auth=True)
        Cheking.check_status_code(result_get, 200)

    """Дублирование доски"""
    @allure.description("Duplicate a board")
    def test_duplicate_a_board(self, board_data):
        print("Метод POST")
        board_id = board_data["boardId"]
        result_post: Response = Microboard_board_api.duplicate_a_board(board_id, "", board_id, use_auth=True)
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['newBoardId'])
        Cheking.check_string_is_uuid(result_post, 'newBoardId')
        assert result_post.json().get('newBoardId') != board_id

        check_post = result_post.json()
        self.newBoardId = check_post.get('newBoardId')

        print("Метод Get")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(self.newBoardId, use_auth=True)
        Cheking.check_status_code(result_get, 200)


    """Переименование доски"""
    @allure.description("Rename a board")
    def test_rename_a_board(self, board_data):
        print("Метод PATCH")
        board_id = board_data["boardId"]
        result_patch: Response = Microboard_board_api.rename_a_board(board_id, "Example", use_auth=True)
        Cheking.check_status_code(result_patch, 200)

        print("Метод GET")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(board_id, use_auth=True)
        Cheking.check_status_code(result_get, 200)


    """Удаление доски"""
    @allure.description("Delete a board")
    def test_delete_a_board(self, board_data):
        print("Метод DELETE")
        board_id = board_data["boardId"]
        result_delete: Response = Microboard_board_api.delete_a_board(board_id, use_auth=True)
        Cheking.check_status_code(result_delete, 204)

        print("Метод Get")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(board_id, use_auth=True)
        Cheking.check_status_code(result_get, 404)


