import pygame
import pygame

class Rock(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.image = pygame.transform.scale(self.image,(49,49))
        #self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def setRockPosicao(self,matriz,grid_rect,tela):
        for i in range(0,len(matriz)):
            for j in range(0,len(matriz)):
                if matriz[i][j] == 3:
                    self.rect.center = grid_rect[i][j]
                    sprite_group = pygame.sprite.Group()
                    sprite_group.add(self)
                    sprite_group.draw(tela)
