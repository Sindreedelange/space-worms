from src.controller.BoardController import BoardController
from src.utils.BoardFactory import BoardFactory
from src.model.Player import Player
from src.utils.Dice import Dice


def main():
    board_factory = BoardFactory()
    board_controller = BoardController()

    board = board_factory.get_board("2")
    board_controller.populate_board(board)
    print("Populate board done")
    for square in board.squares:
        print("Main method: ", square.number)

    dice = Dice()
    player_1 = Player('1', board.squares[board.start_square_number])
    print("Player 1 is at square: ", player_1.square.number)
    roll = dice.dice_roll()
    print("Rolled ", roll)
    move_to_square = board.squares[roll+1]
    player_1.square = move_to_square
    print("Player 1 is now at square: ", player_1.square.number)

main()

