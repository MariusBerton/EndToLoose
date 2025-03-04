from random import randint
from Cards import Cards


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

    def choice(self):
        if self.behaviour == 2 and len(self.hand) > 2:
            for card in self.hand:
                if card.id == 4 or card.id == 5:
                    card.use()
                    return card.discard()
        elif self.behaviour == 3:
            for card in self.hand:
                if card.id == 2 or card.id == 3:
                    card.use()
                    return card.discard()
        else:
            card = self.hand[randint(0, len(self.computer.hand)-1)]
            return card.use()
