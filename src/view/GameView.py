class GameView:

    @staticmethod
    def initial_menu():
        """"""
        print("-----------------------")
        print("Welcome to Space Worms")
        print("-----------------------")
        print("Menu")
        print("Press 1 to play game")
        print("Press 0 to exit game")
        pass

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