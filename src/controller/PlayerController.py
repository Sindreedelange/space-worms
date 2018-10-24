from src.utils.Dice import Dice


class PlayerController:

    @staticmethod
    def player_roll(player):
        print("Player ", player.p_id, " is at square: ", player.square.number)
        roll = Dice.roll()
        print("Rolled ", roll)
        return roll
