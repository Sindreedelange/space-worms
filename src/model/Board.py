import requests
from .Square import Square


class Board(object):

    def __init__(self, data):
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









