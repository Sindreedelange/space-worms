class GameView:

    # Error messages
    # ---------------------------------------------------------------------
    @staticmethod
    def zero_players():
        print("Pretty sure you have to be > 0 players to play this game")

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
        print("It is player ", player.p_id, "'s turn")

    @staticmethod
    def players_standing(players):
        for player in players:
            print("Player ", player.p_id, " is currently at square ", player.square.number)

    @staticmethod
    def wormhole_encounter(player, board):
            print("Square ", player.square.number, " has a wormhole")
            wormhole_number = player.square.wormhole
            if player.square.number > wormhole_number:
                print("Oh oh *Snake noise*")
            else:
                print("Yaho (Super Mario 64-style) *Climbing noise*")
            print("You moved from ", player.square.number)
            player.square = board.squares[wormhole_number-1]
            print("to ", player.square.number, " because of wormhole")
            print("Player ", player.p_id, " is now at square: ", player.square.number)
    # ---------------------------------------------------------------------