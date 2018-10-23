import requests
from src.model.Square import Square


class BoardController(object):

    def __init__(self):
        pass

    def populate_board(self, board):
        response = requests.get(board.start__square_api_ref)
        if response.status_code != 200:
            print("Something wrong with API call \n Try again?")
            return None
        else:
            data = response.json()
            first_square = Square(data)
            board.squares.append(first_square)

            self.traverse_board(board, first_square)

    def traverse_board(self, board, first_square):
        current_square = first_square
        while current_square.has_next():
            current_square = self.get_next_square(current_square)
            if current_square is not None:
                board.squares.append(current_square)
                print(current_square.number)

    @staticmethod
    def get_next_square(square):
        next_square_ref = ""
        for links in square.links:
            if links['direction'] == 'next':
                next_square_ref = links['url']

        response = requests.get(next_square_ref)
        if response.status_code != 200:
            print("Something wrong with API call \n Try again?")
            return None
        else:
            data = response.json()
            next_square = Square(data)
            return next_square
