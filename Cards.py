class Cards:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def __repr__(self):
        return "id : {} | name : {}\n".format(self.id, self.name)


cartes = {
    "nothing": Cards("nothing", 0),
    "draw_1": Cards("draw1", 1),
    "draw_2": Cards("draw2", 2),
    "draw_3": Cards("draw3", 3),
    "discard_1": Cards("discard1", 4),
    "discard_3": Cards("discard2", 5),
    "show": Cards("show", 6),
    "reveal": Cards("reveal", 7),
    "exchange": Cards("exchange", 8)
}
