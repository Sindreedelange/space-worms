import requests
import sys
from Square import Square
import json


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
            self.squares = []
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

    def populate_board(self):
        response = requests.get(self.start__square_api_ref)
        data_response = response.json()
        print(data_response)
        number = data_response['number']
        pos_x = data_response['posX']
        pos_y = data_response['posY']
        name = data_response['name']
        links = data_response['links']
        try:
            wormhole = data_response['wormhole']
            wormhole_url = data_response['wormhole_url']
            new_square = Square(number, pos_x, pos_y, name, links, wormhole, wormhole_url)
        except KeyError:
            new_square = Square(number, pos_x, pos_y, name, links)

        self.squares.append(new_square)






