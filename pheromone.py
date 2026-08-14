import pygame

class Pheromone:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.strength = 1.0

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (80, 130, 220),
            self.position,
            3
        )

    def update(self, dt):
        self.strength -= 0.2 * dt