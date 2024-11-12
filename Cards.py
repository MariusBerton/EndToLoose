from Player import Player


class Cards:
    def __init__(self, name: str) -> None:
        self.name = name

    
    def draw(self, user):
        user.draw()


    def discard(self, user, opponent):
        opponent.discard()


    def punch(self):
        print("You punched your opponent")