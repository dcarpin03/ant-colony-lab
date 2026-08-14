#Punto de entrada de la simulación
import pygame
from ant import Ant

#Inicializa componentes necesarios
pygame.init()   

#Variables que guardan los límites del mundo
WIDTH = 800
HEIGHT = 600

#Crear ventana con unas dimensiones en screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

#Título de la ventana
pygame.display.set_caption("Ant Colony Lab")    

# Reloj para controlar el paso del tiempo en la simulación
clock = pygame.time.Clock()

FPS = 60

#Lista de hormigas
ants = [
    Ant(400, 300),
    Ant(420, 300),
    Ant(380, 300)
]

dt = 0  #Tiempo desde la última actualización

running = True
while running:
    #Recorre uno por uno todos los eventos que ocurren
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    for ant in ants:
        ant.update(dt, WIDTH, HEIGHT)

    #Dibujar la pantalla de negro
    screen.fill((30,30,30))

    for ant in ants:
        ant.draw(screen)

    #Actualizar ventana con el dibujo
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()