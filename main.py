import pygame
import time

from Gridcontainer import GridContainer
from Grid import Grid
from turtle import Turtle
from rock import  Rock
from worm import Worm
from random import randint
from AstarAlgoritmo import aStar
tela =  pygame.display.set_mode([600,480]);
tela.fill([203, 237, 216])
container = GridContainer()
grid = Grid()
tartaruga = Turtle(25,25,(92 + 262),(27+262),(255,255,255))
rock = Rock(25,25,(92 + 262),(27+262),(255,255,255))
worm = Worm(25,25,(92 + 262),(27+262),(255,255,255))
grid.CriandoMatriz();

sprite_group = pygame.sprite.Group()
sprite_group.add(tartaruga)

container.Desenhacontainer(tela)
grid.DesenhaGrid(tela)

tartaruga.setPosicaoInicial(8,8,grid.rectMap)
worm.setWormPosicao(grid.matriz,grid.rectMap,tela)
rock.setRockPosicao(grid.matriz,grid.rectMap,tela)




sprite_group.draw(tela)
pygame.display.flip()

terminado = False
while True:
    if terminado == False:
        turtleMov = aStar(tartaruga.gridPos, worm.gridPos, grid.matriz);
        for i in turtleMov:
            time.sleep(0.5)
            tartaruga.MovimentaTartaruga(str(i))
            ### detecta a colisão se o sprite da tartaruga sair do container do grid
            if not container.rect.collidepoint(tartaruga.rect.x, tartaruga.rect.y):
                #colisão com a borda esquerda
                if (i == 4):
                    tartaruga.MovimentaTartaruga("3")
                # colisão com a borda superior
                elif (i == 1):
                    tartaruga.MovimentaTartaruga("2")
                # colisão com a borda direita
                elif (i == 3):
                    tartaruga.MovimentaTartaruga("4")
                # colisão com a borda inferior
                elif (i == 2):
                    tartaruga.MovimentaTartaruga("1")



            tela.fill([203, 237, 216])
            container.Desenhacontainer(tela)
            grid.DesenhaGrid(tela)
            sprite_group.draw(tela)
            rock.setRockPosicao(grid.matriz, grid.rectMap, tela)
            worm.setWormPosicao(grid.matriz, grid.rectMap, tela)
            pygame.display.flip()
            time.sleep(0.1)
            event = pygame.event.poll()

        terminado = True
        tela.fill([203, 237, 216])
        container.Desenhacontainer(tela)
        grid.DesenhaGrid(tela)
        sprite_group.draw(tela)
        rock.setRockPosicao(grid.matriz, grid.rectMap, tela)
        pygame.display.flip()
        time.sleep(0.1)
    time.sleep(1)
    event = pygame.event.poll()
    #if event.type == pygame.MOUSEBUTTONDOWN:
    if event.type == pygame.QUIT:
        break


