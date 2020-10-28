import pygame
class Grid(object):
    def __init__(self):
        self.x = 80
        self.y = 15
        self.largura = 50
        self.altura = 50



    def DesenhaGrid(self,tela):
        for i in range(0, 9):
            for j in range(0, 9):
                pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(self.x,self.y,self.largura,self.altura),1)
                self.x += 50
            self.x = 80
            self.y += 50

        self.x = 80
        self.y = 15
        self.largura = 50
        self.altura = 50