from random import randint, choose


class Computer:
    def __init__(self, behaviour: int, deck: list) -> None:
        self.behaviour = behaviour  # 1 = random, 2 = agressive, 3 = defensive
        self.deck = deck
        self.hand = []
        self.discard_pile = []

    def act(self):
        choose(self.hand)  # à évoluer

    def use(self):
        pass  # besion d'avancer sur Cards

    def discard(self):
        card = randint(0, len(self.hand) - 1)
        self.discard_pile.append(self.hand[card])
        self.hand.pop(card)

    def draw(self):
        card = self.deck[-1]
        self.hand.append(card)
        self.deck.pop(-1)
