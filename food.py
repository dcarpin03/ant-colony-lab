import pygame

class Food:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (70, 180, 90),
            self.position,
            15
        )