#Punto de entrada de la simulación
import pygame
from ant import Ant

#Inicializa componentes necesarios
pygame.init()   

#Crear ventana con unas dimensiones en screen 
screen = pygame.display.set_mode((800,600)) 

#Título de la ventana
pygame.display.set_caption("Ant Colony Lab")    

# Reloj para controlar el paso del tiempo en la simulación
clock = pygame.time.Clock()

FPS = 60

ant = Ant(400, 300)
dt = 0  #Tiempo desde la última actualización

running = True
while running:
    #Recorre uno por uno todos los eventos que ocurren
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    ant.update(dt)

    #Dibujar la pantalla de negro
    screen.fill((30,30,30))

    ant.draw(screen)

    #Actualizar ventana con el dibujo
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()