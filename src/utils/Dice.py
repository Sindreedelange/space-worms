import random


class Dice(object):
    """Potentially overkill, but increases readability"""

    def __init__(self):
        pass

    @staticmethod
    def roll():
        return random.randint(1, 6)
