from Cards import Cards
from Player import Player
from Computer import Computer
from random import randint, choice


class Game():

    def __init__(self, deck_player: list, deck_computer: list, behaviour: int):
        self.player = Player(deck_player)
        self.computer = Computer(deck_computer, behaviour)

    def end(self):
        if self.player.hand == [] and self.computer.hand == []:
            print("TIE")
        elif self.player.hand == []:
            print("YOU LOST")
        elif self.computer.hand == []:
            print("YOU WON")

    def __str__(self):
        hand = []
        for i in self.player.hand:
            hand.append(repr(i))
        return str(hand)

    def exchange(self):
        self.player.hand, self.computer.hand = self.computer.hand, self.player.hand


game = Game([
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
],
    [
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
],
    1
)

print(game)
for b in range(5):
    game.player.draw()
print(game)
for t in range(2):
    game.computer.draw()
game.exchange()
print(game)
