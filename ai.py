from play import Player
from random import seed
from random import random


class Ai:

    def __init__(self):
        self.random = random()

    def choose_gestures(self):

        seed(Player.gestures)
        self.random = random()
        for gesture in Player.gestures:
             print(gesture)

