from Cards import Cards
from Player import Player
from Computer import Computer
from random import randint, choice


class Game():

    def __init__(self, deck_player, deck_computer, behaviour):
        self.player = Player(deck_player)
        self.computer = Computer(deck_computer, behaviour)

    def end(self):
        if self.player.deck == []:
            print("You lost")
        elif self.computer.deck == []:
            print("you won")
