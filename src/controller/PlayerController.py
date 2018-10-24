from utils.Dice import Dice


class PlayerController:

    @staticmethod
    def player_roll(player):
        roll = Dice.roll()
        print("Rolled ", roll)
        next_square = (roll + player.square.number)
        return next_square
