from random import randint, choice


class Computer:
    def __init__(self, deck: list, behaviour: int,) -> None:
        self.behaviour = behaviour  # 1 = random, 2 = agressive, 3 = defensive
        self.deck = deck
        self.hand = []
        self.discard_pile = []

    def draw(self):
        card = self.deck[-1]
        self.hand.append(card)
        self.deck.pop(-1)

    def discard(self):
        discarded = randint(0, len(self.hand) - 1)
        self.discard_pile.append(self.hand[discarded])
        self.hand.pop(discarded)
