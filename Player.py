from random import randint


class Player:
    def __init__(self, deck: list) -> None:
        self.hand = []
        self.discard_pile = []
        self.deck = deck

    def draw(self):
        card = self.deck[-1]
        self.hand.append(card)
        self.deck.pop(-1)

    def discard(self):
        discarded = randint(0, len(self.hand) - 1)
        self.discard_pile.append(self.hand[discarded])
        self.hand.pop(discarded)
