import pygame


class GridContainer(object):
    def __init__(self):
        self.x = 80
        self.y = 15
        self.largura = 450
        self.altura = 450
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def Desenhacontainer(self, tela):
        pygame.draw.rect(tela, (81, 173, 207), self.rect )

