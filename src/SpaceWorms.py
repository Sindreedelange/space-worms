from src.controller.BoardController import BoardController
from src.utils.BoardFactory import BoardFactory
from src.service.GameService import GameService


def main():
    board_factory = BoardFactory()
    board_controller = BoardController()
    game_service = GameService(board_factory,
                               board_controller)

    game_service.setup()
    game_service.play()


main()


