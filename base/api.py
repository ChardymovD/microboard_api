from base.http_methods import Http_method


base_url = ""
Http_method.set_token("")

"""Методы для тестирования раздела BOARD"""

class Microboard_board_api():

    """Метод для создания доски"""

    @staticmethod
    def create_a_board():
        json_for_create_a_board = {
            "title": "",  # string, nullable: true
            "catalogId": ""  # string($uuid), nullable: true
        }

        post_resource = "/boards"
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_method.post(post_url, json_for_create_a_board)
        print(result_post.text)
        return result_post

    """Метод для удаления доски по ID"""

    @staticmethod
    def delete_a_board(board_id):
        delete_resource = f"/boards/{board_id}"
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = Http_method.delete(delete_url)
        print(result_delete.text)
        return result_delete

    """Метод для получения информации о доске по её ID"""

    @staticmethod
    def get_retrieve_board_details(board_id):
        get_resource = f"/boards/{board_id}/details"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для дублирования доски"""

    @staticmethod
    def duplicate_a_board(board_id):
        json_for_duplicate_a_board = {
            "catalogId": "",  # string($uuid), nullable: true
            "title": ""  # string, nullable: true
        }
        post_resource = f"/boards/{board_id}/duplicate"
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_method.post(post_url, json_for_duplicate_a_board)
        print(result_post.text)
        return result_post

    """Метод для добавления события на доску"""

    @staticmethod
    def add_an_event_to_a_board(board_id):
        json_for_add_an_event_to_a_board = {
            "eventId": "",  # string, *required
            "eventBody": {} # *required
        }
        post_resource = f"/boards/{board_id}/events"
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_method.post(post_url, json_for_add_an_event_to_a_board)
        print(result_post.text)
        return result_post

    """Метод для получения событий с доски"""

    @staticmethod
    def get_retrieve_board_events(board_id):
        get_resource = f"/boards/{board_id}/events"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для переименования доски"""

    @staticmethod
    def rename_a_board(board_id):
        json_for_rename_a_board = {
            "newTitle": ""  # string, *required
        }
        patch_resource = f"/boards/{board_id}"
        patch_url = base_url + patch_resource
        print(patch_url)
        result_patch = Http_method.patch(patch_url, json_for_rename_a_board)
        print(result_patch.text)
        return result_patch