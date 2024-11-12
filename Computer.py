from random import randint


class Computer:
    def __init__(self, behaviour:int) -> None:
        self.behaviour = behaviour  # 1 = random, 2 = agressive, 3 = defensive