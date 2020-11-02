import pygame
import pygame

class Turtle(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        super().__init__()
        self.image = pygame.image.load("turtle.png")
        self.image = pygame.transform.scale(self.image,(49,49))
        #self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.gridPos = 0



    def setPosicaoInicial(self,x,y,matriz):
        self.rect.center = matriz[x][y]
        self.gridPos = (x,y)

    def MovimentaTartaruga(self,tipoMovimento):
        print(tipoMovimento)
        contador = 0
        #movimenta a tartaruga para cima
        if tipoMovimento == "1":
            while(contador < 50):
                self.rect.y -= 10
                contador += 10
        # movimenta a tartaruga para baixo
        elif tipoMovimento == "2":
            while (contador < 50):
                self.rect.y += 10
                contador += 10
        #movimenta a tartaruga para direita
        elif tipoMovimento == "3":
            while (contador < 50):
                self.rect.x += 10
                contador += 10
        # movimenta a tartaruga para esquerda
        elif tipoMovimento == "4":
            while (contador < 50):
                self.rect.x -= 10
                contador += 10