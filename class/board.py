import json
import requests


class Board(object):

    def __init__(self, initialize=True):
        base_url = "https://visningsrom.stacc.com/dd_server_worms/rest/boards/2"
        if initialize:
            data = self.initialize_board(base_url).json()
            self.id = data['id']
            self.name = data['name']
            self.description = data['description']
            self.size = data['size']
            self.dimX = int(data['dimX'])
            self.dimY = int(data['dimY'])
            self.start = int(data['start'])
            self.goal = int(data['goal'])
            self.api_ref = data['self']
            self.start_api_ref = data['startSquare']
        print(self.dimX)

    def initialize_board(self, base_url):
        """ Initialize the board

        Initialize the board using URL for appropriate API

        Args:
            Explain the arguments

        Returns:
            Return type
        """
        response = requests.get(base_url)
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
