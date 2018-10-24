import random


class Dice(object):

    def __init__(self):
        self.eyes = 0

    def dice_roll(self):
        self.eyes = random.randint(1, 6)
