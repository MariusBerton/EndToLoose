import pygame

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Cards:
    def __init__(self, name: str, id: int, image) -> None:
        self.name = name
        self.id = id
        self.image = pygame.transform.scale(image, (120, 150))
        self.rect = image.get_rect()

    def use(self):
        if self.id == 0:
            pass
        elif self.id > 0 and self.id < 4:
            pass

    def __repr__(self):
        return "id : {} | name : {}\n".format(self.id, self.name)

    def draw(self, x, y):
        self.rect.topleft = (x, y)
        SCREEN.blit(self.image, self.rect)


# cartes = {
#     "nothing": Cards("nothing", 0),
#     "draw_1": Cards("draw1", 1),
#     "draw_2": Cards("draw2", 2),
#     "draw_3": Cards("draw3", 3),
#     "discard_1": Cards("discard1", 4),
#     "discard_3": Cards("discard2", 5),
#     "show": Cards("show", 6),
#     "reveal": Cards("reveal", 7),
#     "exchange": Cards("exchange", 8)
# }
