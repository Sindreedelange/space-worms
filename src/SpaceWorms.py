from src.controller.BoardController import BoardController
from src.utils.BoardFactory import BoardFactory
from src.utils.PlayerFactory import PlayerFactory
from src.controller.PlayerController import PlayerController
from src.model.Player import Player


def main():
    board_factory = BoardFactory()
    board_controller = BoardController()

    board = board_factory.get_board("2")
    board_controller.populate_board(board)
    print("Populate board done")
    for square in board.squares:
        print("Main method: ", square.number)

    start_square = board.squares[board.start_square_number-1]
    players = PlayerFactory.initialize_players(2, start_square)
    for player in players:
        print("It is player ", player.p_id, "'s turn")
        to_square_number = PlayerController.player_roll(player)
        player.square = board.squares[to_square_number]
        print("Player ", player.p_id, " is at square: ", player.square.number)

main()

