from src.controller.BoardController import BoardController
from src.utils.BoardFactory import BoardFactory


def main():
    board_factory = BoardFactory()
    board_controller = BoardController()

    board = board_factory.get_board("2")
    board_controller.populate_board(board)
    print("Populate board done")
    for square in board.squares:
        print("Main method: ", square.number)

main()

