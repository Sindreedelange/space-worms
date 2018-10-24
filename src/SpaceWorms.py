from src.controller.BoardController import BoardController
from src.utils.BoardFactory import BoardFactory
from src.utils.PlayerFactory import PlayerFactory
from src.controller.PlayerController import PlayerController


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
        player.square = board.squares[9]
        if hasattr(player.square, 'wormhole'):
            print("Square ", player.square.number, " has a wormhole")
            wormhole_number = player.square.wormhole
            if player.square.number > wormhole_number:
                print("Oh oh *Snake noise*")
            else:
                print("Yahoooo (Super Mario 64-style) *Climbing noise*")
            print("You moved from ", player.square.number)
            player.square = board.squares[wormhole_number-1]
            print("to ", player.square.number, " because of wormhole")
        print("Player ", player.p_id, " is now at square: ", player.square.number)

main()

