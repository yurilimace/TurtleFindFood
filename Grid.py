import pygame
class Grid(object):
    def __init__(self):
        self.x = 80
        self.y = 15
        self.largura = 50
        self.altura = 50
        self.matriz = []
        self.rectMap = []

    def CriandoMatriz(self):
        linha = []
        # 0 ponto final
        # 1 ponto inicial da tartaruga
        # 2 caminho livre
        # 3 caminho bloqueado
        for i in range(0, 9):
            for j in range(0, 9):
                if i == 0 and j == 0:
                    linha.append(0)
                elif i == 7 and j == 8:
                    linha.append(3)
                elif i == 7 and j == 7:
                    linha.append(3)
                elif i == 6 and j == 7:
                    linha.append(3)
                elif i == 5 and j == 5:
                     linha.append(3)
                elif i == 4 and j == 4:
                    linha.append(3)
                elif i == 1 and j == 1:
                    linha.append(3)
                elif i == 2 and j == 1:
                    linha.append(3)
                elif i == 3 and j == 5:
                    linha.append(3)
                else:
                    linha.append(2)
            self.matriz.append(linha)
            linha = []

    def DesenhaGrid(self,tela):
        rect_linha = []
        for i in range(0,len(self.matriz)):
            for j in range(0, len(self.matriz)):
                pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(self.x,self.y,self.largura,self.altura),1)
                rect_linha.append((self.x+25,self.y+25))
                self.x += 50
            self.x = 80
            self.y += 50
            self.rectMap.append(rect_linha)
            rect_linha = []

        self.x = 80
        self.y = 15
        self.largura = 50
        self.altura = 50

