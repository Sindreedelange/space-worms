from src.view.GameView import GameView
from src.utils.PlayerFactory import PlayerFactory
from src.controller.PlayerController import PlayerController
from src.model.Game import Game
from time import sleep


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
        winner = None
        num_rounds = 0
        done = False
        while not done and num_rounds < 20:
            for player in self.game.players:
                GameView.player_pre_roll(player)

                next_square = PlayerController.player_roll(player)

                if self.illegal_move(next_square):
                    GameView.out_of_bounds()
                    continue
                else:
                    player.square = self.game.board.squares[next_square-1]
                    if hasattr(player.square, 'wormhole'):
                        self.wormhole(player)
                    done = self.check_winner(player)
                    if done:
                        winner = player
            print(GameView.players_standing(self.game.players))
            num_rounds += 1
            sleep(1)
        if winner is not None:
            GameView.winner(winner)
        else:
            GameView.end_round()
        exit(0)

    def illegal_move(self, next_square):
        return next_square > self.game.board.size

    def check_winner(self, player):
        return player.square.number == self.game.board.goal_square

    def wormhole(self, player):
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
