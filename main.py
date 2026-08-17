#Punto de entrada de la simulación
import pygame
from ant import Ant
from nest import Nest
from food import Food
from pheromone import Pheromone

#Inicializa componentes necesarios
pygame.init()
font = pygame.font.Font(None, 28)

#Variables que guardan los límites del mundo
WIDTH = 800
HEIGHT = 600
FOOD_DETECTION_RADIUS = 20
NEST_DETECTION_RADIUS = 25
PHEROMONE_INTERVAL = 0.2
PHEROMONE_DETECTION_RADIUS = 40

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

ANT_COUNT = 30

ants = []
pheromones = []

for _ in range(ANT_COUNT):
    ants.append(Ant(nest.position.x, nest.position.y))

dt = 0  #Tiempo desde la última actualización

running = True
while running:
    #Recorre uno por uno todos los eventos que ocurren
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    #Actualizar hormigas
    for ant in ants:
        nearby_pheromones = []

        if ant.carrying_food and ant.pheromone_timer >= PHEROMONE_INTERVAL:
            pheromones.append(
                Pheromone(ant.position.x, ant.position.y)
            )

            ant.pheromone_timer = 0

        ant.update(dt, WIDTH, HEIGHT, nest.position)

        if not ant.carrying_food:
            distance = ant.position.distance_to(food.position)

            for pheromone in pheromones:
                distance_to_pheromone = ant.position.distance_to(pheromone.position)

                if distance_to_pheromone < PHEROMONE_DETECTION_RADIUS:
                    nearby_pheromones.append(pheromone)

            if nearby_pheromones:
                strongest_pheromones = max(
                    nearby_pheromones,
                    key=lambda pheromone: pheromone.strength
                )

                direction_to_pheromone = (
                    strongest_pheromones.position - ant.position
                )

                if direction_to_pheromone.length() > 0:
                    ant.direction = direction_to_pheromone.normalize()

            if distance < FOOD_DETECTION_RADIUS:
                ant.carrying_food = True
        
        else:
            distance_to_nest = ant.position.distance_to(nest.position)
            if distance_to_nest < NEST_DETECTION_RADIUS:
                ant.carrying_food = False
                nest.food_stored += 1

    #Actualizar feromonas
    for pheromone in pheromones:
        pheromone.update(dt)

    #Eliminar las feromonas que ya se han evaporado
    pheromones = [
        pheromone
        for pheromone in pheromones
        if pheromone.strength > 0
    ]


    # ----- DIBUJADO -----

    #Dibujar la pantalla de negro (limpiar pantalla)
    screen.fill((30,30,30))
    
    #Dibujar hormiguero
    nest.draw(screen)

    #Dibujar la fuente de comida
    food.draw(screen)

    for pheromone in pheromones:
        pheromone.draw(screen)

    #Dibujar las hormigas
    for ant in ants:
        ant.draw(screen)

    #Dibujar cantidad comida almacenada
    text = font.render(
        f"Food Stored: {nest.food_stored}",
        True,
        (230, 230, 230)
    )

    screen.blit(text, (15, 15))

    #Actualizar ventana con el dibujo
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()