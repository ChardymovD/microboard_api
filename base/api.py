from base.http_methods import Http_method


base_url = "https://registry.microboard.ru/api/v1"
Http_method.set_token("")

"""Методы для тестирования раздела BOARD"""

class Microboard_board_api():

    """Метод для создания доски"""

    @staticmethod
    def create_a_board(title_example, catalogid_example, use_auth = True):
        json_for_create_a_board = {
            "title": f"{title_example}",  # string, nullable: true
            "catalogId": f"{catalogid_example}"  # string($uuid), nullable: true
        }
        post_resource = "/boards"
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_method.post(post_url, json_for_create_a_board, use_auth = use_auth)
        print(result_post.text)
        return result_post

    """Метод для удаления доски по ID"""

    @staticmethod
    def delete_a_board(board_id, use_auth = True):
        delete_resource = f"/boards/{board_id}"
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = Http_method.delete(delete_url, use_auth = use_auth)
        print(result_delete.text)
        return result_delete

    """Метод для получения информации о доске по её ID"""

    @staticmethod
    def get_retrieve_board_details(board_id, use_auth = True):
        get_resource = f"/boards/{board_id}/details"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_method.get(get_url, use_auth = use_auth)
        print(result_get.text)
        return result_get

    """Метод для дублирования доски"""

    @staticmethod
    def duplicate_a_board(board_id, title_example, catalogid_example, use_auth = True):
        json_for_duplicate_a_board = {
            "catalogId": f"{catalogid_example}",  # string($uuid), nullable: true
            "title": f"{title_example}"  # string, nullable: true
        }
        post_resource = f"/boards/{board_id}/duplicate"
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_method.post(post_url, json_for_duplicate_a_board, use_auth = use_auth)
        print(result_post.text)
        return result_post

    """Метод для добавления события на доску"""

    @staticmethod
    def add_an_event_to_a_board(board_id, evevntid_example, eventbody_example, use_auth = True):
        json_for_add_an_event_to_a_board = {
            "eventId": f"{evevntid_example}",  # string, *required
            "eventBody": {eventbody_example} # *required
        }
        post_resource = f"/boards/{board_id}/events"
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_method.post(post_url, json_for_add_an_event_to_a_board, use_auth = use_auth)
        print(result_post.text)
        return result_post

    """Метод для получения событий с доски"""

    @staticmethod
    def get_retrieve_board_events(board_id, use_auth = True):
        get_resource = f"/boards/{board_id}/events"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_method.get(get_url, use_auth = use_auth)
        print(result_get.text)
        return result_get

    """Метод для переименования доски"""

    @staticmethod
    def rename_a_board(board_id, newtitle_example, use_auth = True):
        json_for_rename_a_board = {
            "newTitle": f"{newtitle_example}"  # string, *required
        }
        patch_resource = f"/boards/{board_id}"
        patch_url = base_url + patch_resource
        print(patch_url)
        result_patch = Http_method.patch(patch_url, json_for_rename_a_board, use_auth = use_auth)
        print(result_patch.text)
        return result_patch