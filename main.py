#Punto de entrada de la simulación
import pygame
from ant import Ant
from nest import Nest
from food import Food
from pheromone import Pheromone
from obstacle import Obstacle

## Métodos
def handle_events():
    #Recorre uno por uno todos los eventos que ocurren
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            foods.append(Food(x, y))

    return True


def draw_world():
        #Dibujar la pantalla de negro (limpiar pantalla)
        screen.fill((30,30,30))
        
        #Dibujar hormiguero
        nest.draw(screen)

        #Dibujar las fuentes de comida
        for food in foods:
            food.draw(screen)

        #Dibujar obstáculos
        for obstacle in obstacles:
            obstacle.draw(screen)

        for pheromone in pheromones:
            pheromone.draw(screen)

        #Dibujar las hormigas
        for ant in ants:
            ant.draw(screen)

        #Dibujar cantidad comida almacenada
        food_gained = font.render(
            f"Food Stored: {nest.food_stored}",
            True,
            (230, 230, 230)
        )

        #Calcular cantidad comida total
        total_food_remaining = sum(
            food.amount
            for food in foods
        )

        # Dibujar cantidad comida restante
        food_remaining = font.render(
            f"Food remaining: {total_food_remaining}",
            True,
            (230, 230, 230)
        )

        screen.blit(food_gained, (15, 15))
        screen.blit(food_remaining, (15, 45))

def update_ants(dt, ants, pheromones, nest, foods, obstacles):
    #Actualizar hormigas
    for ant in ants:
        nearby_pheromones = []

        # Actualizar comportamiento / dirección
        ant.update(dt, nest.position)

        # Si busca comida, percibe el entorno y las feromonas
        if not ant.carrying_food:
            for pheromone in pheromones:
                distance_to_pheromone = ant.position.distance_to(pheromone.position)

                if distance_to_pheromone < PHEROMONE_DETECTION_RADIUS:
                    nearby_pheromones.append(pheromone)

            # Elegimos feromona más alejada del hormiguero
            if nearby_pheromones:
                target_pheromones = max(
                    nearby_pheromones,
                    key=lambda pheromone: pheromone.position.distance_to(nest.position)
                )

                direction_to_pheromone = (
                    target_pheromones.position - ant.position
                )

                if direction_to_pheromone.length() > 0:
                    target_direction = direction_to_pheromone.normalize()

                    ant.direction += (
                        target_direction * PHEROMONE_INFLUENCE * dt
                    )

                    ant.direction = ant.direction.normalize()

        
        # Mover después de recibir la dirección 
        ant.move(dt, WIDTH, HEIGHT, obstacles)

        # Comprobar interacciones después del movimiento
        if not ant.carrying_food:
            for food in foods:
                distance_to_food = ant.position.distance_to(food.position)

                if distance_to_food < FOOD_DETECTION_RADIUS and food.amount > 0:
                    ant.carrying_food = True
                    food.amount -= 1
                    break
        
        else:
            distance_to_nest = ant.position.distance_to(nest.position)

            if distance_to_nest < NEST_DETECTION_RADIUS:
                ant.carrying_food = False
                nest.food_stored += 1

        # Si vuelve con comida, dejar feromonas
        if ant.carrying_food and ant.pheromone_timer >= PHEROMONE_INTERVAL:
            pheromones.append(
                Pheromone(
                    ant.position.x,
                    ant.position.y
                )
            )

            ant.pheromone_timer = 0

def update_pheromones(dt, pheromones):
    #Actualizar feromonas
    for pheromone in pheromones:
        pheromone.update(dt)

    #Eliminar las feromonas que ya se han evaporado
    return [
        pheromone
        for pheromone in pheromones
        if pheromone.strength > 0
    ]


#Inicializa componentes necesarios
pygame.init()
font = pygame.font.Font(None, 28)

#CONSTANTES
WIDTH = 800
HEIGHT = 600
FOOD_DETECTION_RADIUS = 20
NEST_DETECTION_RADIUS = 25
PHEROMONE_INTERVAL = 0.2
PHEROMONE_DETECTION_RADIUS = 40
PHEROMONE_INFLUENCE = 2.0

#Crear hormiguero en el centro
nest = Nest(WIDTH / 2, HEIGHT / 2)

#Crear fuentes de comida
foods = [
    Food(650, 200),
    Food(150, 150),
    Food(650, 500)
]

#Crear obstáculos
obstacles = [
    Obstacle(250, 180, 120, 30),
    Obstacle(500, 380, 30, 120)
]

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
    #Capturar eventos
    running = handle_events()

    #Actualizar hormigas y feromonas
    update_ants(dt, ants, pheromones, nest, foods, obstacles)
    pheromones = update_pheromones(dt, pheromones)

    # ----- DIBUJADO -----
    draw_world()

    #Actualizar ventana con el dibujo
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()