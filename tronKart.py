import pygame
import random
from operator import itemgetter as getall
from player import Player

BASE_SPEED = 8
BASE_DIRECTION = random.randint(0, 359)
BACKGROUND_COLOR = (0, 0, 0)

SPEED_INCREMENT = 1
ANGLE_INCREMENT = 5

PKEYS_UP = [pygame.K_w, pygame.K_UP]
PKEYS_DOWN = [pygame.K_s, pygame.K_DOWN]
PKEYS_LEFT = [pygame.K_a, pygame.K_LEFT]
PKEYS_RIGHT = [pygame.K_d, pygame.K_RIGHT]


class TronKart:
    def __init__(self, width: int = 1200, height: int = 800, fps: int = 60,
                 title: str = "Tron Kart") -> None:
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = BACKGROUND_COLOR
        hurricane = pygame.image.load("images/hurricane.png")
        self.player = Player(self.width / 2, self.height / 2,
                             BASE_DIRECTION, BASE_SPEED, hurricane)
        pygame.init()

    def run(self) -> None:
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()

        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    break

            keys = pygame.key.get_pressed()
            if any(getall(*PKEYS_UP)(keys)):  # Speed up
                self.player.change_speed(SPEED_INCREMENT)
            if any(getall(*PKEYS_DOWN)(keys)):  # Slow down
                self.player.change_speed(-SPEED_INCREMENT)
            if any(getall(*PKEYS_LEFT)(keys)):  # Turn left
                self.player.change_direction(ANGLE_INCREMENT)
            if any(getall(*PKEYS_RIGHT)(keys)):  # Turn right
                self.player.change_direction(-ANGLE_INCREMENT)

            self.window.fill(self.bgColor)
            self.player.update(self.width, self.height)
            self.player.draw(self.window)
            pygame.display.update()

            clock.tick(self.fps)

        pygame.quit()
