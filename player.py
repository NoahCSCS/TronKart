import math
import pygame
from trail import Trail

MIN_SPEED: int = 6
MAX_SPEED: int = 16
BLUE: (int, int, int) = (0, 0, 255)
TRAIL_WIDTH: int = 5
IMAGE_SCALE: int = (100, 100)


class Player:
    def __init__(self, x, y, direction_angle, speed, image):
        self.x = x
        self.y = y
        self.direction_angle = direction_angle
        self.speed = speed
        self.image = pygame.transform.scale(image, IMAGE_SCALE)
        self.rect = self.image.get_rect()
        self.trail = Trail(BLUE, TRAIL_WIDTH)

    def change_direction(self, angle_change):  # angle is in degrees
        self.direction_angle = (self.direction_angle + angle_change) % 360

    def change_speed(self, speed_change):
        self.speed = max(min(self.speed + speed_change, MAX_SPEED), MIN_SPEED)

    def update(self, width, height):
        self.x = (self.x + self.speed * math.cos(math.radians(self.direction_angle))) % width
        self.y = (self.y - self.speed * math.sin(math.radians(self.direction_angle))) % height # minus because y is inverted (pygame dumb)
        self.trail.add_point((self.x, self.y))

    def draw(self, window):
        self.trail.draw(window)
        window.blit(self.image,
                    (self.x - self.image.get_width() / 2,
                     self.y - self.image.get_height() / 2))
