from Cards import Cards
from Player import Player
from Computer import Computer
from random import randint, choice


def first():
    players = ["player", "computer"]
    if choice(players) == "player":
        print("You start")
        priority = True
    else:
        print("The opponent starts")
        priority = False
    return priority

    
def turn():
    pass