class GameView:

    # Error messages
    # ---------------------------------------------------------------------
    @staticmethod
    def few_players():
        print("Pretty sure you have to be > 1 players to play this game")

    @staticmethod
    def invalid_initial_menu():
        print("Please input either 0 or 1")

    @staticmethod
    def too_many_players():
        print("Too many players, please try again")

    @staticmethod
    def quit_game():
        print("Bye Felicia")

    @staticmethod
    def not_a_valid_number():
        print("Please input a natural number")

    @staticmethod
    def out_of_bounds():
        print("Almost stepped out of the board there")
    # ---------------------------------------------------------------------

    # Menus
    # ---------------------------------------------------------------------
    @staticmethod
    def initial_menu():
        return ("-----------------------\n"
                "Welcome to Space Worms\n"
                "-----------------------\n"
                "_________MENU_________\n"
                "Press 1 to play game\n"
                "Press 0 to exit game\n")

    @staticmethod
    def game_menu():
        return ("-----------------------\n"
                "_______GAME MENU_______\n"
                "-----------------------\n"
                "Currently only 1 map available: Original\n"
                "Please input number of players: \n"
                "(Between 1 and 4) \n")
    # ---------------------------------------------------------------------

    # Player actions
    # ---------------------------------------------------------------------
    @staticmethod
    def player_pre_roll(player):
        print("It's player ", player.p_id, "'s turn")

    @staticmethod
    def players_standing(players):
        for player in players:
            print("Player ", player.p_id, " is currently at square ", player.square.number)

    @staticmethod
    def wormhole_encounter(player):
            print("Square ", player.square.number, " has a wormhole")

    # ---------------------------------------------------------------------

    # Other
    @staticmethod
    def setting_up_game():
        print("Currently setting up game, please wait")

    @staticmethod
    def done_setting_up_game(game):
        print("Ready to play game with ", len(game.players), " number of players, on board ", game.board.name)

    @staticmethod
    def snake():
        print("Oh oh *Snake noise*")

    @staticmethod
    def ladder():
        print("Yaho (Super Mario 64-style) *Climbing noise*")

    @staticmethod
    def winner(player):
        print("Congratz, player ", player.p_id, "\n Terminating")

    @staticmethod
    def end_round():
        print("Sorry, round limit exceeded \n Terminating")
