import pygame

#Entidad hormiga para agrupar los datos y el comportamiento de cada hormiga
class Ant:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.direction = pygame.Vector2(1, 0).normalize()
        self.speed = 100

    #Actualizar estado del objeto
    def update(self, dt):
        self.position += self.direction * self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (220, 180, 80),
            self.position,
            10
        )
