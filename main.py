from Cards import Cards
from Player import Player
from Computer import Computer
from random import randint, shuffle, choice


class Game():

    def __init__(self, deck_player: list, deck_computer: list, behaviour: int):
        self.player = Player(deck_player)
        self.computer = Computer(deck_computer, behaviour)

    def setup(self):
        shuffle(self.player.deck)
        shuffle(self.computer.deck)
        for i in range(5):
            self.player.draw()
            self.computer.draw()

    def order(self):
        choice = input("head or tails ?\n")
        if choice == "head" or choice == "tails":
            print("Flipping the coin")
            coin = self.flip()
            print(f"{coin} !")
            if coin == choice:
                print("You start")
                return True
            else:
                print("The opponent starts")
                return False
        else:
            return self.order()

    def playerTurn(self):
        print("Your turn")
        print("Choose a card")
        card = int(input(f"{self.player.hand}\n"))
        print(self.player.hand[card-1])

    def computerTurn(self):
        print("The opponent's turn")
        print("Choosing a card")
        print(self.computer.hand[randint(0, len(self.computer.hand)-1)])

    def isHandEmpty(self):
        return self.player.hand == [] or self.computer == []

    def exchange(self):
        self.player.hand, self.computer.hand = self.computer.hand, self.player.hand

    def flip(self):
        return choice(["head", "tails"])

    def __repr__(self):
        return "Hand : {}\n".format(self.player.hand)


starting_deck = [
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("nothing", 0),
    Cards("draw1", 1),
    Cards("draw1", 1),
    Cards("draw1", 1),
    Cards("draw1", 1),
    Cards("draw1", 1),
    Cards("draw1", 1),
    Cards("draw2", 2),
    Cards("draw2", 2),
    Cards("draw2", 2),
    Cards("draw2", 2),
    Cards("draw2", 2),
    Cards("draw3", 3),
    Cards("draw3", 3),
    Cards("discard1", 4),
    Cards("discard1", 4),
    Cards("discard1", 4),
    Cards("discard1", 4),
    Cards("discard1", 4),
    Cards("discard2", 5),
    Cards("discard2", 5),
    Cards("discard2", 5),
    Cards("reveal", 6),
    Cards("reveal", 6),
    Cards("reveal", 6),
    Cards("reveal", 7),
    Cards("exchange", 8)
]


def launch_game():
    game = Game(starting_deck, starting_deck, 1)
    game.setup()
    turn_order = game.order()
    if turn_order == True:
        game.playerTurn()
    else:
        game.computerTurn()
