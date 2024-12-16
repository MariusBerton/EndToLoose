from random import randint


class Cards:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id


cartes = {
    "nothing": Cards("nothing", 0),
    "draw_1": Cards("draw1", 1),
    "draw_2": Cards("draw2", 2),
    "draw_3": Cards("draw3", 3),
    "discard_1": Cards("discard1", 4),
    "discard_3": Cards("discard2", 5),
    "reveal": Cards("reveal", 6),
    "exchange": Cards("exchange", 7)
}
