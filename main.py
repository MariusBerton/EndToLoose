from Cards import Cards
from Player import Player
from Computer import Computer
from random import randint, choice


class Game():

    def __init__(self, deck_player, deck_computer, behaviour):
        self.player = Player(deck_player)
        self.computer = Computer(deck_computer, behaviour)


def first():
    players = ["player", "computer"]
    if choice(players) == "player":
        print("You start")
        priority = True
    else:
        print("The opponent starts")
        priority = False
    return priority


def turn(player, computer, priority):
    if priority == True:
        player.act()
        computer.act()
    else:
        computer.act()
        player.act()
