import pygame
import random

#Entidad hormiga para agrupar los datos y el comportamiento de cada hormiga
class Ant:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.direction = pygame.Vector2(-1, -1).normalize()

        self.speed = 100
        self.turn_speed = 90

    #Actualizar estado del objeto
    def update(self, dt):
        #Grados de giro random
        turn = random.uniform(-self.turn_speed, self.turn_speed)
        self.direction = self.direction.rotate(turn * dt)
        self.position += self.direction * self.speed * dt

        margin = 10

        if self.position.x <= margin:
            self.position.x = margin
            self.direction.x *= -1

        elif self.position.x >= 800 - margin:
            self.position.x = 800 - margin
            self.direction.x *= -1

        if self.position.y <= margin:
            self.position.y = margin
            self.direction.y *= -1

        elif self.position.y >= 600 - margin:
            self.position.y = 600 - margin
            self.direction.y *= -1


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
