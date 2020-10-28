import pygame
import time

from Gridcontainer import GridContainer
from Grid import Grid
from turtle import Turtle

from random import randint

tela =  pygame.display.set_mode([600,480]);
tela.fill([203, 237, 216])
container = GridContainer()
grid = Grid()
tartaruga = Turtle()


container.Desenhacontainer(tela)
grid.DesenhaGrid(tela)
tartaruga.desenhaTurtle(tela)

pygame.display.flip()

while True:
    tipoMovimento = randint(1,4)
    ### detecta se não colide na borda superior e esquerda do grid container
    if not container.rect.collidepoint(tartaruga.rect.x - 5, tartaruga.rect.y - 5):
        print("bateu na borda superior ou esquerda")
        if (backup == 4):
            print("entrou")
            tartaruga.MovimentaTartaruga("3")
        elif (backup == 1):
            tartaruga.MovimentaTartaruga("2")
            ### detecta se não colide na borda inferior ou direita do grid container
    elif not container.rect.collidepoint(tartaruga.rect.x + 30, tartaruga.rect.y + 30):
        print("bateu na borda inferior ou direita")
        if (backup == 3):
            tartaruga.MovimentaTartaruga("4")
        elif (backup == 2):
            tartaruga.MovimentaTartaruga("1")

    else:
        tartaruga.MovimentaTartaruga(str(tipoMovimento))

    tela.fill([203, 237, 216])
    container.Desenhacontainer(tela)
    grid.DesenhaGrid(tela)
    tartaruga.desenhaTurtle(tela)
    backup = tipoMovimento
    pygame.display.flip()
    time.sleep(0.5)
    event = pygame.event.poll()

    #if event.type == pygame.MOUSEBUTTONDOWN:


    if event.type == pygame.QUIT:
        break


