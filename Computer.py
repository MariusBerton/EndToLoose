from random import randint, choose


class Computer:
    def __init__(self, behaviour: int, deck: list) -> None:
        self.behaviour = behaviour  # 1 = random, 2 = agressive, 3 = defensive
        self.deck = deck
        self.hand = []
        self.discard_pile = []

    def draw(self, card):
        for i in range(card.id):
            card = self.deck[-1]
            self.hand.append(card)
            self.deck.pop(-1)

    def discard(self, card):
        for i in range(card.id - 3):
            discarded = randint(0, len(self.hand) - 1)
            self.discard_pile.append(self.hand[card])
            self.hand.pop(card)
