import pygame
import random

#Entidad hormiga para agrupar los datos y el comportamiento de cada hormiga
class Ant:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)

        angle = random.uniform(0, 360)
        self.direction = pygame.Vector2(1, 0).rotate(angle)

        self.speed = 100
        self.turn_speed = 90

        self.carrying_food = False

        self.pheromone_timer = 0

    #Actualizar estado del objeto
    def update(self, dt, nest_position):
        if self.carrying_food:
            direction_to_nest = nest_position - self.position

            if direction_to_nest.length() > 0:
                self.direction = direction_to_nest.normalize()
        else:
            #Grados de giro random
            turn = random.uniform(-self.turn_speed, self.turn_speed)
            self.direction = self.direction.rotate(turn * dt)
        
        self.pheromone_timer += dt

    def move(self, dt, world_width, world_height):
        self.position += self.direction * self.speed * dt
        
        margin = 10

        if self.position.x <= margin:
            self.position.x = margin
            self.direction.x *= -1

        elif self.position.x >= world_width - margin:
            self.position.x = world_width - margin
            self.direction.x *= -1

        if self.position.y <= margin:
            self.position.y = margin
            self.direction.y *= -1

        elif self.position.y >= world_height - margin:
            self.position.y = world_height - margin
            self.direction.y *= -1
        

    def draw(self, screen):
        head_position = self.position + self.direction * 6
        adbomen_position = self.position - self.direction * 5

        if self.carrying_food:
            color = (230, 90, 70)
        else:
            color = (220, 180, 80)

        pygame.draw.circle(
            screen,
            color,
            adbomen_position,
            6
        )

        pygame.draw.circle(
            screen,
            (220, 180, 80),
            head_position,
            4
        )
