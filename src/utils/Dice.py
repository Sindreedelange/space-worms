import random


class Dice:

    @staticmethod
    def roll():
        return random.randint(1, 6)
