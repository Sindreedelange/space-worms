import requests
from src.model.Board import Board


class BoardFactory(object):

    def __init__(self, base_url="https://visningsrom.stacc.com/dd_server_worms/rest/boards/"):
        self.base_url = base_url

    def get_board(self, board_id):
        url = self.base_url + board_id
        response = self.initialize_board(url)
        if response is not None:
            data = response.json()
            return Board(data)
        else:
            return

    @staticmethod
    def initialize_board(url):
        """
        Initialize the board

        Initialize the board using pre-defined URL

        :return: requests.models.response
        """
        response = requests.get(url)
        if response.status_code != 200:
            print("Something wrong with API call \n Try again?")
            return None
        else:
            return response

