import numpy
from random import randint
import time

def CriandoMatriz(matriz):
    linha = []
    for i in range(0,9):
        for j in range(0,9):
            if i == 0 and j == 0:
                linha.append(0)
            elif i == 5 and j == 5:
                linha.append(1)
            else:
                linha.append(2)
        matriz.append(linha)
        linha = []

def PrintaMatriz(matriz):
    for i in matriz:
            print(i)



def aStar():
    pontoFinal = [0,0]
    pontoInicial = [5,5]
    distanciaP = numpy.linalg.norm(numpy.array(pontoInicial)-numpy.array(pontoFinal))
    caminho = []
    movimento = []
    caminho.append(pontoInicial)
    loop = True
    while(loop):
        distancias = []
        pontos = []
        animacao = []
        #verificar a casa de cima
        ponto1 = [pontoInicial[0]-1,pontoInicial[1]]
        if(ponto1[0] >= 0):
            pontos.append(ponto1)
            animacao.append(1)
            distancias.append(numpy.linalg.norm(numpy.array(ponto1) - numpy.array(pontoFinal)))
        #verificar  a casa de baixo
        ponto1 = [pontoInicial[0]+1, pontoInicial[1]]
        if(ponto1[0] < 9):
            distancias.append(numpy.linalg.norm(numpy.array(ponto1) - numpy.array(pontoFinal)))
            pontos.append(ponto1)
            animacao.append(2)
        #verificar a casa de direita
        ponto1 = [pontoInicial[0], pontoInicial[1]+1]
        if(ponto1[1] < 9):
            distancias.append(numpy.linalg.norm(numpy.array(ponto1)-numpy.array(pontoFinal)))
            pontos.append(ponto1)
            animacao.append(3)
        #verificar a casa da esquerda
        ponto1 = [pontoInicial[0], pontoInicial[1] - 1]
        if(ponto1[1]>=0):
            distancias.append(numpy.linalg.norm(numpy.array(ponto1)-numpy.array(pontoFinal)))
            pontos.append(ponto1)
            animacao.append(4)
        #print(pontos)

        #remove se o caminho estiver dentro de pontos
        if len(caminho) > 0:
            for i in caminho:
                if i in pontos:
                    index = pontos.index(i)
                    pontos.remove(i)
                    del(animacao[index])
                    del(distancias[index])



        # index da menor distancia calculada comparada com a distancia P
        low = distancias.index(min(distancias))
        caminho.append(pontos[low])
        movimento.append(animacao[low])
        pontoInicial = pontos[low]
        distanciaP = numpy.linalg.norm(numpy.array(pontoInicial) - numpy.array(pontoFinal))

        if(pontoFinal == pontoInicial):
            print("caminho pronto")
            print(caminho)
            loop = False;
            break;

    return movimento







def main():
    matriz = []
    CriandoMatriz(matriz)
    #PrintaMatriz(matriz)
    #print(matriz)
    #pontoA = numpy.array((1,1))
    #pontoB = numpy.array((10,10))
    #print(pontoA[0])
    turtle = aStar()
    print(turtle)

main()