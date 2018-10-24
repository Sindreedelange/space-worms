from model.Player import Player


class PlayerFactory:

    @staticmethod
    def initialize_players(n_players, start_square):
        players = []
        for i in range(n_players):
            new_player = Player(i, start_square)
            players.append(new_player)
        return players
