from Cards import Cards
from Player import Player
from Computer import Computer
from time import sleep
from random import shuffle, randint
import pygame
import sys
import os


ASSETS = os.path.join(os.getcwd(), "assets")

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
BEIGE = (208, 176, 139)
BLUE = (17, 50, 67, 255)

# images


def load_card_images():
    if not os.path.exists(ASSETS):
        print(f"Error: assets file not found {ASSETS}.")
        sys.exit()

    card_files = [
        os.path.join(ASSETS, file)
        for file in os.listdir(ASSETS)
        if file.endswith(".png") and file != "back.png"
    ]

    if not card_files:
        print("Error : no image files found in the assets folder.")
        sys.exit()

    return [pygame.image.load(card) for card in card_files]


def load_back_image():
    back = os.path.join(ASSETS, "back.png")
    if not os.path.exists(back):
        print(f"Error: image 'back.png' cannot be found.")
        sys.exit()
    return pygame.image.load(back)


def load_background():
    background = os.path.join(ASSETS, "fond.png")
    if not os.path.exists(background):
        print(f"Error")
        sys.exit()
    return pygame.image.load(background)


background_image = pygame.transform.scale(load_background(), (WIDTH, HEIGHT))


def draw_card_slot(x, y, width, height, image=None, is_hovered=False):
    if image:
        if is_hovered:
            enlarged_image = pygame.transform.scale(
                image, (280, 350))
            SCREEN.blit(enlarged_image, (x - 100, y - 200))
        else:
            SCREEN.blit(image, (x, y))


def get_card_positions(start_x, y, hand, max_width=800, min_space=50, max_space=100):
    card_width = 120
    if len(hand) > 1:
        space = min(max_space, max(
            min_space, max_width // (len(hand) - 1)))
    else:
        space = 0
    return [(start_x + i * space, y) for i in range(len(hand))]


def display_rules_screen():
    rules_text = [
        "Rules of the game :",
        "1. Choose a card.",
        "2. Apply it's effect.",
        "3. Now it's your opponent's turn.",
        "4. The first one to empty his hand loose.",
        "5. Enjoy."
    ]

    font_menu = os.path.join(ASSETS, "SHOWG.TTF")
    if not os.path.exists(font_menu):
        print(f"Error: Font file SHOWG.TTF not found in {ASSETS}.")
        sys.exit()

    font = pygame.font.Font(font_menu, 40)
    back_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 60)

    while True:
        SCREEN.fill(BEIGE)
        for i, line in enumerate(rules_text):
            text_surface = font.render(line, True, BLACK)
            SCREEN.blit(text_surface, (WIDTH // 2 -
                        text_surface.get_width() // 2, 100 + i * 50))

        pygame.draw.rect(SCREEN, BLUE, back_button)
        back_text = font.render("Back", True, BEIGE)
        SCREEN.blit(back_text, (back_button.x + 50, back_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return

        pygame.display.update()


def display_home_screen():
    font_menu = os.path.join(ASSETS, "SHOWG.TTF")
    if not os.path.exists(font_menu):
        print(f"Error: Font file SHOWG.TTF not found in {ASSETS}.")
        sys.exit()
    SCREEN.blit(background_image, (0, 0))

    font = pygame.font.Font(font_menu, 74)

    END = font.render("End", True, BLUE)
    TO = font.render("To", True, BLUE)
    LOOSE = font.render("Loose", True, BLUE)

    button_width = 200
    button_height = 60

    button_spacing = 50  # Augmente l'espace horizontal entre les boutons

    play_button = pygame.Rect(WIDTH // 2 - (button_width * 1.5) -
                              button_spacing, HEIGHT // 2, button_width, button_height)
    rules_button = pygame.Rect(
        WIDTH // 2 - (button_width // 2), HEIGHT // 2, button_width, button_height)
    quit_button = pygame.Rect(WIDTH // 2 + (button_width * 0.5) +
                              button_spacing, HEIGHT // 2, button_width, button_height)

    while True:
        SCREEN.blit(background_image, (0, 0))

        SCREEN.blit(END, (WIDTH // 2 - END.get_width() //
                    2, HEIGHT // 4 - 80))
        SCREEN.blit(TO, (WIDTH // 2 - TO.get_width() //
                    2, HEIGHT // 4 + 10))
        SCREEN.blit(LOOSE, (WIDTH // 2 - LOOSE.get_width() //
                    2, HEIGHT // 4 + 100))

        pygame.draw.rect(SCREEN, BLUE, play_button)
        pygame.draw.rect(SCREEN, BLUE, rules_button)
        pygame.draw.rect(SCREEN, BLUE, quit_button)

        button_font = pygame.font.Font(font_menu, 50)
        PLAY = button_font.render("Play", True, BEIGE)
        RULES = button_font.render("Rules", True, BEIGE)
        QUIT = button_font.render("Quit", True, BEIGE)

        SCREEN.blit(PLAY, (play_button.x + 50, play_button.y + 10))
        SCREEN.blit(RULES, (rules_button.x + 30, rules_button.y + 10))
        SCREEN.blit(QUIT, (quit_button.x + 50, quit_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return
                elif rules_button.collidepoint(event.pos):
                    display_rules_screen()
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def display_end_screen(message):
    font = pygame.font.Font(font_menu, 100)
    text = font.render(message, True, WHITE)

    alpha = 0  # Commence transparent
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(BLACK)

    while alpha < 255:
        fade_surface.set_alpha(alpha)
        SCREEN.blit(background_image, (0, 0))
        SCREEN.blit(
            text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
        SCREEN.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)
        alpha += 5

    pygame.time.delay(2000)  # Pause 2 secondes
    display_home_screen()


def setup(player, computer):
    shuffle(player.deck)
    shuffle(computer.deck)
    for i in range(5):
        player.draw()
        computer.draw()


def use(player, computer, user: bool, card: Cards):
    if card.id < 4 and card.id > 0:
        for _ in range(card.id):
            if user == True:
                player.draw()
            else:
                computer.draw()
    elif card.id > 3 and card.id < 6:
        for i in range(card.id - 3):
            if user == True:
                computer.discard()
            else:
                player.discard()
    elif card.id == 6:
        pass
    elif card.id == 7:
        pass
    elif card.id == 8:
        player.hand, computer.hand = computer.hand, player.hand

    def isHandEmpty(self):
        return self.player.hand == [] or self.computer == []


global back_image
card_images = load_card_images()
back_image = pygame.transform.scale(load_back_image(), (120, 150))


# deck
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


font_menu = os.path.join(ASSETS, "SHOWG.TTF")
back_button = pygame.Rect(WIDTH - 170, HEIGHT - 70, 140, 40)
button_font = pygame.font.Font(font_menu, 50)

# boucle


def main():

    player = Player(starting_deck)
    computer = Computer(starting_deck, randint(1, 3))
    setup(player, computer)

    player1slots = get_card_positions(280, 520, computer.hand)
    player2slots = get_card_positions(280, 50, player.hand)

    middle_slot = (585, 300)
    middle_card = None

    font_menu = os.path.join(ASSETS, "SHOWG.TTF")
    button_font = pygame.font.Font(font_menu, 30)

    while True:
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background_image, (0, 0))

        back_text, new_game_text = button_font.render(
            "Back", True, BEIGE),  button_font.render("New Game", True, BEIGE)
        back_width, new_game_width = back_text.get_width() + \
            20, new_game_text.get_width() + 20
        back_height, new_game_height = 50, 50
        back_x, new_game_x = WIDTH - back_width - \
            20, WIDTH - new_game_width - 20
        back_y, new_game_y = HEIGHT - 2 * back_height - \
            40, HEIGHT - new_game_height - 20
        back_button, new_game_button = pygame.Rect(
            back_x, back_y, back_width, back_height), pygame.Rect(new_game_x, new_game_y, new_game_width, new_game_height)

        pygame.draw.rect(SCREEN, BLUE, back_button)
        SCREEN.blit(back_text, (back_x + (back_width - back_text.get_width()) // 2,
                                back_y + (back_height - back_text.get_height()) // 2))

        pygame.draw.rect(SCREEN, BLUE, new_game_button)
        SCREEN.blit(new_game_text, (new_game_x + (new_game_width - new_game_text.get_width()) // 2,
                                    new_game_y + (new_game_height - new_game_text.get_height()) // 2))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        draw_card_slot(1100, 50, 120, 150, image=back_image)
        if len(player.hand) > 0:
            player2slots = [(280 + i * 50, 50)
                            for i in range(len(player.hand))]

        for i, _ in enumerate(player.hand):
            is_hovered = pygame.Rect(
                player2slots[i][0], player2slots[i][1], 120, 150).collidepoint(mouse_x, mouse_y)
            draw_card_slot(player2slots[i][0], player2slots[i][1],
                           120, 150, image=back_image, is_hovered=is_hovered)

        if middle_card:
            draw_card_slot(middle_slot[0], middle_slot[1],
                           120, 150, image=middle_card.image)

        draw_card_slot(60, 520, 120, 150, image=back_image)
        for i, carte in enumerate(computer.hand):
            is_hovered = pygame.Rect(
                player1slots[i][0], player1slots[i][1], 120, 150).collidepoint(mouse_x, mouse_y)
            draw_card_slot(player1slots[i][0], player1slots[i][1],
                           120, 150, image=carte.image, is_hovered=is_hovered)

        def handle_card_click(hand, slots):
            if not hand:
                return None

            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, (x, y) in enumerate(slots):
                card_rect = pygame.Rect(x, y, 120, 150)
                if card_rect.collidepoint(mouse_x, mouse_y):
                    if i < len(hand):
                        return hand.pop(i)
            return None

        if not player.hand:
            display_end_screen("You Win!")
            return

        elif not computer.hand:
            display_end_screen("You Loose!")
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    display_home_screen()
                elif new_game_button.collidepoint(event.pos):
                    main()

                clicked_card = handle_card_click(
                    player.hand, player1slots)
                if clicked_card:
                    use(player, computer, True, clicked_card)
                    middle_card = clicked_card

                    pygame.display.update()
                    pygame.time.delay(500)
                    card_bot = handle_card_click(
                        computer.hand, player1slots)
                    if card_bot:
                        use(player, computer, False, card_bot)
                        middle_card = card_bot

        pygame.display.flip()


display_home_screen()
main()
