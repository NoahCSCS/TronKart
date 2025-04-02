import pygame

MAX_POINTS = 40


class Trail:
    def __init__(self, color, width, max_points: int = MAX_POINTS):
        self.color = color
        self.width = width
        self.points = []
        self.max_points = max_points

    def add_point(self, point: (float, float)) -> None:
        self.points.append(point)
        if len(self.points) > self.max_points:
            self.points.pop(0)

    def draw(self, window):
        for point in self.points:
            pygame.draw.circle(window, self.color, point, self.width)
        # if len(self.points) > 1:
        #     pygame.draw.lines(window, self.color, False, self.points, self.width)
