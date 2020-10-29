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
tartaruga = Turtle(25,25,(92 + 262),(27+262),(255,255,255))

sprite_group = pygame.sprite.Group()
sprite_group.add(tartaruga)

container.Desenhacontainer(tela)
grid.DesenhaGrid(tela)


sprite_group.draw(tela)
pygame.display.flip()


while True:
    tipoMovimento = randint(1,4)
    tartaruga.MovimentaTartaruga(str(tipoMovimento))
    ### detecta a colisão se o sprite da tartaruga sair do container do grid
    if not container.rect.collidepoint(tartaruga.rect.x, tartaruga.rect.y):
        #colisão com a borda esquerda
        if (tipoMovimento == 4):
            tartaruga.MovimentaTartaruga("3")
        # colisão com a borda superior
        elif (tipoMovimento == 1):
            tartaruga.MovimentaTartaruga("2")
        # colisão com a borda direita
        elif (tipoMovimento == 3):
            tartaruga.MovimentaTartaruga("4")
        # colisão com a borda inferior
        elif (tipoMovimento == 2):
            tartaruga.MovimentaTartaruga("1")




    tela.fill([203, 237, 216])
    container.Desenhacontainer(tela)
    grid.DesenhaGrid(tela)
    sprite_group.draw(tela)
    pygame.display.flip()
    time.sleep(0.5)
    event = pygame.event.poll()

    #if event.type == pygame.MOUSEBUTTONDOWN:


    if event.type == pygame.QUIT:
        break


