import pygame

#Entidad hormiga para agrupar los datos y el comportamiento de cada hormiga
class Ant:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.direction = pygame.Vector2(-1, -1).normalize()
        self.speed = 100

    #Actualizar estado del objeto
    def update(self, dt):
        self.position += self.direction * self.speed * dt

    def draw(self, screen):
        
        head_position = self.position + self.direction * 6
        adbomen_position = self.position - self.direction * 5

        pygame.draw.circle(
            screen,
            (220, 180, 80),
            adbomen_position,
            6
        )

        pygame.draw.circle(
            screen,
            (220, 180, 80),
            head_position,
            4
        )
