#Punto de entrada de la simulación
import pygame

#Inicializa componentes necesarios
pygame.init()   

#Crear ventana con unas dimensiones en screen 
screen = pygame.display.set_mode((800,600)) 

#Título de la ventana
pygame.display.set_caption("Ant Colony Lab")    

# Reloj para controlar el paso del tiempo en la simulación
clock = pygame.time.Clock()

FPS = 60
x = 400
y = 300

running = True
while running:
    #Recorre uno por uno todos los eventos que ocurren
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    x += 1

    #Dibujar la pantalla de negro
    screen.fill((30,30,30))

    pygame.draw.circle(
        screen,
        (220, 180, 80),
        (x, y),
        10
    )

    #Actualizar ventana con el dibujo
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()