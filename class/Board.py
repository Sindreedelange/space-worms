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
        response = requests.get(self.start__square_api_ref).json()
        first_square = self.serialize_json_square(response)
        self.squares.append(first_square)

        self.traverse_board(first_square)

    def traverse_board(self, first_square):
        square = first_square
        while square.number != 68:
            square = self.get_next_square(square)
            self.squares.append(square)

    def get_next_square(self, square):
        next_square_ref = ""
        for links in square.links:
            if links['direction'] == 'next':
                next_square_ref = links['url']

        response = requests.get(next_square_ref).json()
        next_square = self.serialize_json_square(response)
        return next_square

    def serialize_json_square(self, response):
        number = response['number']
        pos_x = response['posX']
        pos_y = response['posY']
        name = response['name']
        links = response['links']
        try:
            wormhole = response['wormhole']
            wormhole_url = response['wormhole_url']
            new_square = Square(number, pos_x, pos_y, name, links, wormhole, wormhole_url)
        except KeyError:
            new_square = Square(number, pos_x, pos_y, name, links)

        return new_square

    def check_last_square(self, square):
        cont = False
        for links in square.links:
            if links['direction'] == 'next' and links['square'] <= self.goal_square:
                cont = True
            else:
                cont = False
        return cont









