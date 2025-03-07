from Cards import Cards
from Player import Player
from Computer import Computer
from random import randint, shuffle, choice
import pygame
import random
import sys
import os

# chemin vers dossier assets
ASSETS_DIR = os.path.join(os.getcwd(), "assets")

pygame.init()

# taille de la fenetre
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("End to Loose")

# couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BEIGE = (240, 229, 207, 255)
BLUE = (17, 50, 67, 255)

# les images de cartes


def load_card_images():
    if not os.path.exists(ASSETS_DIR):
        print(
            f"Error: assets file not found {ASSETS_DIR}.")
        sys.exit()

    card_files = [
        os.path.join(ASSETS_DIR, file)
        for file in os.listdir(ASSETS_DIR)
        if file.endswith(".png") and file != "back.png"
    ]

    if not card_files:
        print("Error : no image files found in the assets folder.")
        sys.exit()

    return [pygame.image.load(card) for card in card_files]


# l'image de dos de carte

def load_back_image():
    back_path = os.path.join(ASSETS_DIR, "back.png")
    if not os.path.exists(back_path):
        print(f"Error: image 'back.png' cannot be found.")
        sys.exit()
    return pygame.image.load(back_path)


# def draw_card_slot(x, y, width, height, text="", color=None, image=None):
#     if color:
#         pygame.draw.rect(SCREEN, color, (x, y, width, height), 3)
#     if text:
#         font = pygame.font.Font(None, 36)
#         label = font.render(text, True, WHITE)
#         SCREEN.blit(label, (x + 15, y + 15))
#     if image:
#         SCREEN.blit(image, (x, y))


def draw_card_slot(x, y, width, height, image=None, is_hovered=False):
    if image:
        if is_hovered:
            enlarged_image = pygame.transform.scale(
                image, (140, 175))  # Agrandir
            SCREEN.blit(enlarged_image, (x - 10, y - 10))  # Décaler légèrement
        else:
            SCREEN.blit(image, (x, y))

def display_home_screen():
    # Charger la police
    font_menu = os.path.join(ASSETS_DIR, "SHOWG.TTF")
    if not os.path.exists(font_menu):
        print(f"Error: Font file SHOWG.TTF not found in {ASSETS_DIR}.")
        sys.exit()

    font = pygame.font.Font(font_menu, 74)

    title1 = font.render("End", True, BLUE)
    title2 = font.render("To", True, BLUE)
    title3 = font.render("Loose", True, BLUE)

    button_width = 200
    button_height = 60

    loose_pos_y = HEIGHT // 4 + 100

    button_start_y = loose_pos_y + title3.get_height() + 50

    horizontal_spacing = 50
    total_button_width = 2 * button_width + horizontal_spacing

    play_button = pygame.Rect(
        WIDTH // 2 - total_button_width // 2, button_start_y, button_width, button_height)

    quit_button = pygame.Rect(
        play_button.right + horizontal_spacing, button_start_y, button_width, button_height)

    while True:
        SCREEN.fill(BEIGE)

        SCREEN.blit(title1, (WIDTH // 2 - title1.get_width() //
                    2, HEIGHT // 4 - 80))
        SCREEN.blit(title2, (WIDTH // 2 - title2.get_width() //
                    2, HEIGHT // 4 + 10))
        SCREEN.blit(title3, (WIDTH // 2 - title3.get_width() //
                    2, HEIGHT // 4 + 100))

        pygame.draw.rect(SCREEN, BLUE, play_button)
        pygame.draw.rect(SCREEN, BLUE, quit_button)

        button_font = pygame.font.Font(font_menu, 50)
        start_text = button_font.render("Play", True, BEIGE)
        quit_text = button_font.render("Quit", True, BEIGE)

        SCREEN.blit(start_text, (play_button.x + play_button.width // 2 - start_text.get_width() // 2,
                                 play_button.y + play_button.height // 2 - start_text.get_height() // 2))
        SCREEN.blit(quit_text, (quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2,
                                quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


class Game():

    def __init__(self, deck_player: list, deck_computer: list, behaviour: int):
        self.player = Player(deck_player)
        self.computer = Computer(deck_computer, behaviour)

    def setup(self):
        shuffle(self.player.deck)
        shuffle(self.computer.deck)
        for i in range(5):
            self.player.draw()
            self.computer.draw()

    # def order(self):
    #     choice = input("head or tails ?\n")
    #     if choice == "head" or choice == "tails":
    #         print("Flipping the coin")
    #         coin = self.flip()
    #         print(f"{coin} !")
    #         if coin == choice:
    #             print("You start")
    #             return True
    #         else:
    #             print("The opponent starts")
    #             return False
    #     else:
    #         return self.order()

    def playerTurn(self):
        print("Your turn")
        print("Choose a card")
        card = int(input(f"{self.player.hand}\n"))
        print(self.player.hand[card-1])

    def computerTurn(self):
        print("The opponent's turn")
        print("Choosing a card")
        print(self.computer.choice())

    def isHandEmpty(self):
        return self.player.hand == [] or self.computer == []

    def exchange(self):
        self.player.hand, self.computer.hand = self.computer.hand, self.player.hand

    def flip(self):
        return choice(["head", "tails"])

    def __repr__(self):
        return "Hand : {}\n".format(self.player.hand)


global back_image  # backcard
card_images = load_card_images()
back_image = pygame.transform.scale(load_back_image(), (120, 150))


starting_deck = []
for i in range(9):
    starting_deck.append(Cards("nothing", 0, card_images[0]))
for i in range(6):
    starting_deck.append(Cards("draw1", 1, card_images[1]))
for i in range(5):
    starting_deck.append(Cards("draw2", 2, card_images[2]))
for i in range(2):
    starting_deck.append(Cards("draw3", 3, card_images[3]))
for i in range(5):
    starting_deck.append(Cards("discard1", 4, card_images[4]))
for i in range(3):
    starting_deck.append(Cards("discard2", 5, card_images[5]))
for i in range(3):
    starting_deck.append(Cards("show", 6, card_images[6]))
starting_deck.append(Cards("reveal", 7, card_images[7]))
starting_deck.append(Cards("exchange", 8, card_images[8]))


def launch_game():
    game = Game(starting_deck, starting_deck, 1)
    game.setup()
    # turn_order = game.order()
    # if turn_order == True:
    #     game.playerTurn()
    # else:
    #     game.computerTurn()


# Boucle principale
def main():
    display_home_screen()  # affiche le home

    game = Game(starting_deck, starting_deck, 1)
    game.setup()

    player1slots = [(280 + i * 150, 50) for i in range(5)]
    player2slots = [(280 + i * 150, 520) for i in range(5)]

    middle_slot = (585, 300)
    middle_card = None

    while True:
        SCREEN.fill((0, 0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        draw_card_slot(1100, 50, 120, 150, image=back_image)
        for i, _ in enumerate(game.player.hand):
            is_hovered = pygame.Rect(
               player1slots[i][0], player1slots[i][1], 120, 150).collidepoint(mouse_x, mouse_y)
            draw_card_slot(player1slots[i][0], player1slots[i][1],
                          120, 150, image=back_image, is_hovered=is_hovered)
           
        if middle_card:
            draw_card_slot(middle_slot[0], middle_slot[1],
                           120, 150, image=middle_card.image)


        draw_card_slot(60, 520, 120, 150, image=back_image)
        for i, carte in enumerate(game.computer.hand):
            is_hovered = pygame.Rect(player2slots[i][0], player2slots[i][1], 120, 150).collidepoint(mouse_x, mouse_y)
            draw_card_slot(player2slots[i][0], player2slots[i][1], 120, 150, image=carte.image, is_hovered=is_hovered)

        def handle_card_click(hand, middle_slot):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player_slots = [(280 + i * 150, 520) for i in range(len(hand))]

            for i, (x, y) in enumerate(player_slots):
                card_rect = pygame.Rect(x, y, 120, 150)

                if card_rect.collidepoint(mouse_x, mouse_y):
                    clicked_card = hand.pop(i)
                    return clicked_card  
            return None  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_card = handle_card_click(game.computer.hand, middle_slot)
                if clicked_card:
                    middle_card = clicked_card

        pygame.display.update()


main()
