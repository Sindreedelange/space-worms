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
        """Set up the game

            Get necessary user input to set up board and game
        """

        user_choice = -1
        while user_choice == -1:
            user_choice = self.get_input_initial_menu()

        # The user wants to play
        if user_choice == 1:
            while self.number_players == -1:
                self.number_players = self.get_input_number_players()

            self.set_up_game()
        else:
            GameView.quit_game()
            exit(0)

    def set_up_game(self):
        """Set up the necessary modules board, squares and players"""
        GameView.setting_up_game()
        board = self.set_up_board()
        players = self.set_up_players(board)
        self.game = Game(board, players)
        GameView.done_setting_up_game(self.game)

    def set_up_players(self, board):
        """Set up the players

            Use PlayerFactory to set up the players
        """
        start_square = board.squares[board.start_square_number-1]
        players = PlayerFactory.initialize_players(self.number_players, start_square)
        return players

    def set_up_board(self):
        """Set up the board

            Use BoardFactory to get the board from the API,
            and BoardController to populate the board with its squares
        """
        board = self.board_factory.get_board("2")
        self.board_controller.populate_board(board)
        return board

    def play(self):
        """ Play the game

            The game's getting played without user interaction, however it should
            provide enough feedback for the user to get an overview of the game play
        """
        done = False
        while not done:
            for player in self.game.players:
                GameView.player_pre_roll(player)

                # The player makes a move by rolling the dice
                next_square = PlayerController.player_roll(player)

                # Checking if the user's move would put them outside the board, if so handle it
                if self.illegal_move(next_square):
                    GameView.out_of_bounds()
                    next_square = self.make_illegal_move_legal(player, next_square)

                player.square = self.game.board.squares[next_square-1]
                if hasattr(player.square, 'wormhole'):
                    self.wormhole(player)
                done = self.check_winner(player)
                if done:
                    winner = player
                    GameView.winner(winner)
                    break
            GameView.players_standing(self.game.players)
            sleep(1)
        exit(0)

    def make_illegal_move_legal(self, player, illegal_square):
        """ Make a legal move out of an illegal one

        When a player rolls the dice so that their next square is out of bounds,
        the program makes calculation so that basically the player walks to the last square,
        and whatever is left of number of steps, they walk backwards, from the last square.
        Ref. README (Game rules)
        """
        GameView.try_access_illegal_square(illegal_square)
        # Calculate number of steps from the end of board
        roll = illegal_square - player.square.number
        distance_to_end = self.game.board.size - player.square.number
        remaining = roll - distance_to_end
        legal_square_number = self.game.board.size - remaining
        GameView.information_legal_square(legal_square_number)
        return legal_square_number

    def illegal_move(self, next_square):
        """Verify if a move is legal, or not"""
        return next_square > self.game.board.size

    def check_winner(self, player):
        """Verify if a player is located at goal square"""
        return player.square.number == self.game.board.goal_square

    def wormhole(self, player):
        """A player has landed on a square the has a wormhole

            This means that the player will be 'transported' to the wormhole's number.
            This could either land the player further ahead on the board, or farther back.
            Visually, when playing the board game, this depends on if the wormhole is a
            'snake' (back) or 'ladder' (forward)
        """
        GameView.wormhole_encounter(player)
        wormhole_number = player.square.wormhole
        if player.square.number > wormhole_number:
            GameView.snake()
        else:
            GameView.ladder()
        player.square = self.game.board.squares[wormhole_number - 1]

    # Get input
    # ---------------------------------------------------------------------
    def get_input_number_players(self):
        """Get number of desired players

            Query the user for number of desired players [2, 5]
        """
        user_choice = input(GameView.game_menu())
        if user_choice.isdigit():
            user_choice = int(user_choice)
            return self.validate_input_number_of_players(user_choice)
        else:
            return -1

    def get_input_initial_menu(self):
        """Query user input for initial menu

            Here the user can decide to either start the game, or exit the game
        """
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
        """Validate that the user's menu choice is a valid one"""
        if (user_choice == 0) or (user_choice == 1):
            return user_choice
        else:
            GameView.invalid_initial_menu()
            return -1

    @staticmethod
    def validate_input_number_of_players(user_choice):
        """Validate that the user's menu choice is a valid one"""
        if user_choice == 0 or user_choice == 1:
            GameView.few_players()
            return -1
        elif user_choice > 4:
            GameView.too_many_players()
            return -1
        else:
            return user_choice
    # ---------------------------------------------------------------------
