import pygame

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Cards:
    def __init__(self, name: str, id: int, image) -> None:
        self.name = name
        self.id = id
        self.image = pygame.transform.scale(image, (120, 150))
        self.rect = image.get_rect()

    def __repr__(self):
        return "id : {} | name : {}\n".format(self.id, self.name)

    def draw(self, x, y):
        self.rect.topleft = (x, y)
        SCREEN.blit(self.image, self.rect)
