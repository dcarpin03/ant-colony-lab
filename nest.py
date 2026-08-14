import pygame

class Nest:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (120, 80, 45),
            self.position,
            25
        )