import pygame as p
import sys
import random
import spritesheet
import slots

WIDTH = HEIGHT = 600
CENTER = (WIDTH // 2, HEIGHT // 2)
CELL_SIZE = 96
ROWS = 3
COLUMNS = 3
MAX_FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class SlotMachine:
    """Overall class to manage slot assets and behavior"""

    def __init__(self):
        """Initialize the program"""

        # Initialize pygame and font
        p.init()
        p.font.init()
        # Create one font fot the button text and a slightly bigger font when the button inflates
        self.my_font = p.font.SysFont("calibri", 30)
        self.big_font = p.font.SysFont("calibri", 40)
        # Create the screen and clock
        self.screen = p.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(p.Color("Green"))
        self.clock = p.time.Clock()
        self.sprite_image = p.image.load("images/Symbols.png").convert_alpha()
        self.symbols = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        # Initialize the rectangles for the button
        self.spin = p.Rect(0, 0, 0, 0)
        # Initialize the slot settings
        self.slot_state = slots.slots()
        # Set up the initial bet
        self.bet_amount = self.slot_state.min_bet
        # Randomize the starting position of each reel
        for i in range(len(self.symbols)):
            self.symbols[i] = self.randomize(
            self.slot_state.reels[i], self.slot_state.weights[i], ROWS
            )
        # Keeps track of player's winnings
        self.total_amount = 10000
        self.winnings = 0

    def run(self):
        """The main loop for the program to run in"""

        while True:
            # Get the mouse position
            self.pos = p.mouse.get_pos()
            # Event loop
            for e in p.event.get():
                if e.type == p.QUIT:
                    sys.exit()
                elif e.type == p.MOUSEBUTTONDOWN:
                    if self.button_collision(self.spin, self.pos):
                        self.randomize_all()
                        self.total_amount -= self.bet_amount
                    self.win(self.symbols)
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_UP:
                        if self.bet_amount + self.slot_state.bet_inc <= self.slot_state.max_bet:
                            self.bet_amount += self.slot_state.bet_inc
                    elif e.key == p.K_DOWN:
                        if self.bet_amount - self.slot_state.bet_inc >= self.slot_state.min_bet:
                            self.bet_amount -= self.slot_state.bet_inc
                    elif e.key == p.K_SPACE:
                        self.winnings = 0
                        for x in range(100000):
                            self.total_amount -= self.bet_amount
                            self.randomize_all()
                            self.winnings += self.win(self.symbols)
                        print(self.winnings / (self.bet_amount * 1000000))


            ss = spritesheet.SpriteSheet(self.sprite_image)
            self.sprites = ss.create_image_list(32, 32, 3, BLACK)
            self.screen.fill(p.Color("Green"))
            self.create_window(ROWS, COLUMNS)
            self.display_multi_reels(ROWS, COLUMNS, self.symbols, self.screen)
            # Flag to determine if the buttons are inflated or not
            self.spin_inflate = True if self.button_collision(self.spin, self.pos) else False
            self.spin = self.create_button(
                self.screen,
                self.my_font,
                self.big_font,
                "Spin",
                p.Color("black"),
                (CENTER[0], CENTER[1] + 210),
                100,
                50,
                p.Color("yellow"),
                self.spin_inflate,
            )
            self.create_text(self.screen, str(self.bet_amount), self.my_font, p.Color("Black"), (50, 50))
            self.create_text(self.screen, str(self.total_amount), self.my_font, p.Color("Black"), (WIDTH - 50, 50))
            self.clock.tick(MAX_FPS)
            p.display.flip()

    def create_window(self, rows, columns):
        """Creates the window for the slot machine"""

        start = (
            CENTER[1] - ((rows / 2) * CELL_SIZE),
            CENTER[0] - ((columns / 2) * CELL_SIZE),
        )
        for i in range(rows):
            for j in range(columns):
                p.draw.rect(
                    self.screen,
                    WHITE,
                    p.Rect(
                        start[1] + (j * CELL_SIZE),
                        start[0] + (i * CELL_SIZE),
                        CELL_SIZE,
                        CELL_SIZE,
                    ),
                )

    def display_single_reel(self, rows, columns, symbols, screen, reel_num):
        """Tells the program what symbols to display on what stops"""

        start = (
            CENTER[1] - ((rows / 2) * CELL_SIZE),
            CENTER[0] - ((columns / 2) * CELL_SIZE) + ((reel_num - 1) * CELL_SIZE),
        )

        for i in range(len(symbols)):
            screen.blit(
                self.sprites[symbols[i]], (start[1], start[0] + (i * CELL_SIZE))
            )

    def display_multi_reels(self, rows, columns, symbols, screen):
        """Displays symbols on all the stops"""

        for i in range(len(symbols)):
            self.display_single_reel(rows, columns, symbols[i], screen, i + 1)

    def randomize(self, reel, weight, window_h):
        """Picks a random symbol on the reel"""

        result = []
        weight_total = 0
        for i in weight:
            weight_total += i
        x = random.randint(1, weight_total)
        weight_total = 0
        for i in range(len(weight)):
            weight_total += weight[i]
            if x <= weight_total:
                result += [reel[i]]
                for j in range(window_h // 2):
                    result = (
                        [reel[(i - (j + 1)) % len(reel)]]
                        + result
                        + [reel[(i + (j + 1)) % len(reel)]]
                    )
                break
        return result

    def randomize_all(self):
        """Randomizes all reels"""

        for i in range(len(self.symbols)):
            self.symbols[i] = self.randomize(
            self.slot_state.reels[i], self.slot_state.weights[i], ROWS
            )


    def create_button(
        self,
        screen,
        font,
        big_font,
        text,
        text_color,
        button_center,
        button_width,
        button_height,
        button_color,
        inflate,
    ):
        """Creates a button centered at a point with a font rect in the middle"""
        font_surf = (
            font.render(text, False, text_color)
            if not inflate
            else big_font.render(text, False, text_color)
        )
        font_width, font_height = font_surf.get_size()
        offset = 15 if inflate else 0
        button_rect = p.Rect.inflate(
            p.Rect(0, 0, button_width, button_height), offset, offset
        )
        button_rect.center = button_center
        p.draw.rect(screen, button_color, button_rect)
        font_rect = p.Rect(0, 0, font_width, font_height)
        font_rect.center = button_rect.center
        screen.blit(font_surf, font_rect)
        return button_rect

    def button_collision(self, rect, mouse):
        """Returns true if mouse is over rect"""
        return True if rect.collidepoint(mouse[0], mouse[1]) else False

    def create_text(self, screen, text, font, color, center):
        """Creates text on the screen"""
        font_surf = font.render(text, False, color)
        font_width, font_height = font_surf.get_size()
        font_rect = p.Rect(0, 0, font_width, font_height)
        font_rect.center = center
        screen.blit(font_surf, font_rect)

    def win(self, symbols):
        """Determines if slot wins"""

        middle = len(symbols[0]) // 2
        win_sym = symbols[0][middle]
        for i in range(len(symbols) - 1):
            flag = True
            if symbols[i + 1][middle] != win_sym:
                flag = False
                break
        if flag == True:
            self.total_amount += self.bet_amount * self.slot_state.paytable[symbols[0][middle]]
            return self.bet_amount * self.slot_state.paytable[symbols[0][middle]]
        return 0






if __name__ == "__main__":
    slot = SlotMachine()
    slot.run()
