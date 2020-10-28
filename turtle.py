import pygame
class Turtle(object):
    def __init__(self):
        self.x = 92 + 260
        self.y = 27 + 260
        self.largura = 25
        self.altura = 25
        self.rect = pygame.Rect(self.x,self.y,self.largura,self.altura)

    def desenhaTurtle(self,tela):
        pygame.draw.rect(tela, (255, 255, 255),self.rect)

    def MovimentaTartaruga(self,tipoMovimento):
        print(tipoMovimento)
        #movimenta a tartaruga para cima
        if tipoMovimento == "1":
            self.rect.y -= 10
        # movimenta a tartaruga para baixo
        elif tipoMovimento == "2":
            self.rect.y += 10
        #movimenta a tartaruga para direita
        elif tipoMovimento == "3":
            self.rect.x += 10
        # movimenta a tartaruga para esquerda
        elif tipoMovimento == "4":
            self.rect.x -= 10