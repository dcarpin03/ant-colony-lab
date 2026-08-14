#Punto de entrada de la simulación
import pygame
from ant import Ant
from nest import Nest
from food import Food

#Inicializa componentes necesarios
pygame.init()   

#Variables que guardan los límites del mundo
WIDTH = 800
HEIGHT = 600
FOOD_DETECTION_RADIUS = 20

#Crear hormiguero en el centro
nest = Nest(WIDTH / 2, HEIGHT / 2)
food = Food(650, 200)

#Crear ventana con unas dimensiones en screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

#Título de la ventana
pygame.display.set_caption("Ant Colony Lab")    

# Reloj para controlar el paso del tiempo en la simulación
clock = pygame.time.Clock()

FPS = 60

ANT_COUNT = 5

ants = []

for _ in range(ANT_COUNT):
    ants.append(Ant(nest.position.x, nest.position.y))

dt = 0  #Tiempo desde la última actualización

running = True
while running:
    #Recorre uno por uno todos los eventos que ocurren
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    for ant in ants:
        ant.update(dt, WIDTH, HEIGHT)

        if not ant.carrying_food:
            distance = ant.position.distance_to(food.position)

            if distance < FOOD_DETECTION_RADIUS:
                ant.carrying_food = True
                print("¡Una hormiga ha recogido comida!")

    #Dibujar la pantalla de negro (limpiar pantalla)
    screen.fill((30,30,30))
    
    #Dibujar hormiguero
    nest.draw(screen)

    #Dibujar la fuente de comida
    food.draw(screen)

    #Dibujar las hormigas
    for ant in ants:
        ant.draw(screen)

    #Actualizar ventana con el dibujo
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()