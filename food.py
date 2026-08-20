import pygame

class Food:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.amount = 50
        self.max_amount = 50

    def draw(self, screen):
        if self.amount <= 0:
            return

        min_radius = 4
        max_radius = 15

        ratio = self.amount / self.max_amount
        radius = min_radius + (max_radius - min_radius) * ratio

        pygame.draw.circle(
            screen,
            (70, 180, 90),
            self.position,
            radius
        )