from requests import Response
from base.cheking import Cheking
from base.api import Microboard_board_api


class Test_Board_api():

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
        boardId = check_post.get('boardId')

        print("Метод GET")
        result_get : Response = Microboard_board_api.get_retrieve_board_details(boardId)
        Cheking.check_status_code(result_get, 200)

