from random import randint


class Coin:
    def __init__(self):
        self.faces = 2
        
    
    def flip(self):
        return randnt(1, self.faces) == 1