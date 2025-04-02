import pygame
import math
from player import Player

BASE_SPEED = 8
BASE_DIRECTION = 0
BACKGROUND_COLOR = (0, 0, 0)

SPEED_INCREMENT = 1
ANGLE_INCREMENT = 5

class TronKart:
    def __init__(self, width=1200, height=800, fps=60, title="Tron Kart"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = BACKGROUND_COLOR
        hurricane = pygame.image.load("images/hurricane.png")
        self.player = Player(self.width / 2, self.height / 2, BASE_DIRECTION, BASE_SPEED, hurricane)
        pygame.init()
    
    def run(self):
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
            if keys[pygame.K_w]:
                self.player.change_speed(SPEED_INCREMENT)
            if keys[pygame.K_s]:
                self.player.change_speed(-SPEED_INCREMENT)
            if keys[pygame.K_a]: # Turn left
                self.player.change_direction(ANGLE_INCREMENT)
            if keys[pygame.K_d]: # Turn right
                self.player.change_direction(-ANGLE_INCREMENT) 

            self.window.fill(self.bgColor)
            self.player.update(self.width, self.height)
            self.player.draw(self.window)
            pygame.display.update()

            clock.tick(self.fps)

        pygame.quit()