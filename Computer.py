from random import randint


class Computer:
    def __init__(self, behaviour:int, deck:list) -> None:
        self.behaviour = behaviour  # 1 = random, 2 = agressive, 3 = defensive
        self.deck = deck
        self.hand = []
        self.discard_pile = []