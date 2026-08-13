#Punto de entrada de la simulación
import pygame

#Inicializa componentes necesarios
pygame.init()   

#Crear ventana con unas dimensiones en screen 
screen = pygame.display.set_mode((800,600)) 

#Título de la ventana
pygame.display.set_caption("Ant Colony Lab")    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()