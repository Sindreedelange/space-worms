from src.view.GameView import GameView
from src.utils.PlayerFactory import PlayerFactory
from src.controller.PlayerController import PlayerController
from src.model.Game import Game


class GameService:

    def __init__(self, board_factory, board_controller):
        self.board_factory = board_factory
        self.board_controller = board_controller
        self.game = Game(None, None)
        self.number_players = -1

    def setup(self):
        user_choice = -1
        while user_choice == -1:
            user_choice = self.get_input_initial_menu()

        if user_choice == 1:
            while self.number_players == -1:
                self.number_players = self.get_input_number_players()

            self.set_up_game()
        else:
            GameView.quit_game()
            exit(0)

    def set_up_game(self):
        GameView.setting_up_game()
        board = self.set_up_board()
        players = self.set_up_players(board)
        self.game = Game(board, players)
        GameView.done_setting_up_game(self.game)

    def set_up_players(self, board):
        start_square = board.squares[board.start_square_number-1]
        players = PlayerFactory.initialize_players(self.number_players, start_square)
        return players

    def set_up_board(self):
        board = self.board_factory.get_board("2")
        self.board_controller.populate_board(board)
        return board

    def play(self):
        for player in self.game.players:
            GameView.player_pre_roll(player)
            to_square_number = PlayerController.player_roll(player)
            player.square = self.game.board.squares[to_square_number]
            print(player.square.name)
            if hasattr(player.square, 'wormhole'):
                GameView.wormhole_encounter(player)
                wormhole_number = player.square.wormhole
                if player.square.number > wormhole_number:
                    GameView.snake()
                else:
                    GameView.ladder()
                print("You moved from ", player.square.number)
                player.square = self.game.board.squares[wormhole_number - 1]
                print("to ", player.square.number, " because of wormhole")
                print("Player ", player.p_id, " is now at square: ", player.square.number)
        print(GameView.players_standing(self.game.players))

    # Get input
    # ---------------------------------------------------------------------
    def get_input_number_players(self):
        user_choice = input(GameView.game_menu())
        if user_choice.isdigit():
            user_choice = int(user_choice)
            return self.validate_input_number_of_players(user_choice)
        else:
            return -1

    def get_input_initial_menu(self):
        user_choice = input(GameView.initial_menu())
        if user_choice.isdigit():
            user_choice = int(user_choice)
            return self.validate_input_initial_menu(user_choice)
        else:
            GameView.not_a_valid_number()
            return -1
    # ---------------------------------------------------------------------

    # Input validation
    # ---------------------------------------------------------------------
    @staticmethod
    def validate_input_initial_menu(user_choice):
        if (user_choice == 0) or (user_choice == 1):
            return user_choice
        else:
            GameView.invalid_initial_menu()
            return -1

    @staticmethod
    def validate_input_number_of_players(user_choice):
        if user_choice == 0:
            GameView.zero_players()
            return -1
        elif user_choice > 4:
            GameView.too_many_players()
            return -1
        else:
            return user_choice
    # ---------------------------------------------------------------------
