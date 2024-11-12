from random import randint

class Player:
    def __init__(self, deck:list) -> None:
        self.hand = []
        self.discard_pile = []
        self.deck = deck


    def select(self):
        pass # besion de pygame (donne des infos sur la carte sur laquelle le curseur est)


    def use(self):
        pass # besion d'avancer sur Cards


    def discard(self):
        card = randint(0, len(self.hand) - 1)
        self.discard_pile.append(self.hand[card])
        self.hand.pop(card)


    def draw(self):
        card = self.deck[-1]
        self.hand.append(card)
        self.deck.pop(-1)


    # draw et discard fonctionnent