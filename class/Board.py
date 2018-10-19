import json
import requests


class Board(object):

    def __init__(self, initialize=True):
        self.base_url = "https://visningsrom.stacc.com/dd_server_worms/rest/boards/2"
        if initialize:
            data = self.initialize_board.json()
            self.id = data['id']
            self.name = data['name']
            self.description = data['description']
            self.size = data['size']
            self.dimX = int(data['dimX'])
            self.dimY = int(data['dimY'])
            self.start_square = int(data['start'])
            self.goal_square = int(data['goal'])
            self.api_ref = data['self']
            self.start__square_api_ref = data['startSquare']
        print(self.dimX)

    @property
    def initialize_board(self):
        """
        Initialize the board

        Initialize the board using pre-defined URL

        :return: requests.models.response
        """
        response = requests.get(self.base_url)
        if response.status_code != 200:
            print("Something wrong with API call \n Try again?")
        else:
            return response

    def function(self, param):
        """ Quick description

        In-depth description

        Args:
            Explain the arguments
        
        Returns:
            Return type 
        """


board = Board()
