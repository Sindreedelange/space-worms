from src.view.GameView import GameView
from src.model.Game import Game


class GameController:

    def setup(self, game):
        user_choice = -1
        while user_choice == -1:
            user_choice = self.get_input_initial_menu()

        # User choice = 1 or 0
        if user_choice == 1:
            number_of_players = -1
            while number_of_players == -1:
                number_of_players = self.get_input_number_players()
        else:
            GameView.quit_game()
            exit(0)

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

    # Input validation

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


gc = GameController()
gc.setup(Game(0, 1))
