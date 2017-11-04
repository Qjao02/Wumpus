from random import *
from Espaco import Espaco

class Mapa :
    mapa = []
    nPocos = 0
    listaDePocos = []


    def __init__ (self,wumppus):
        
        #criaMatriz
        for i in range (0,4):
            newList = []
            for j in range(0,4):
                newEspaco = Espaco()
                newList.append(newEspaco)
            self.mapa.append(newList)
        
        self.printMapa()
        
        #cria o wumppus
        self.criarWumppus(wumppus)
    
        #cria os pocos
        self.criarPocos(wumppus)
        

    def printMapa(self):
        print "blabla"
        listPrint = []
        cont = 0
        for i in range(0,len(self.mapa)):
            cont = 0
            for j in range(0, len(self.mapa[i])):
                cont = 0
                listPrint.append('||| ')
                if self.mapa[i][j].wumppus == 1:
                    listPrint.append("wumppus")
                    cont = 1
                if self.mapa[i][j].dinheiro == 1:
                    listPrint.append("ouro")
                    cont = 1
                if self.mapa[i][j].flecha == 1:
                    listPrint.append("flecha")
                    cont = 1
                if self.mapa[i][j].fedo == 1:
                    listPrint.append("fedo")
                    cont = 1
                if self.mapa[i][j].briza == 1:
                    listPrint.append("briza")
                    cont = 1
                if self.mapa[i][j].poco == 1:
                    listPrint.append("poco")
                    cont = 1
                
                if cont == 0:
                    listPrint.append("vazio")
                
                listPrint.append(' |||')
            print listPrint
            listPrint[:] = []
    
    def criarWumppus(self, wumppus):
        
        #adcionaWumppus ao mapa
        self.mapa[wumppus.position[0]][wumppus.position[1]].wumppus = 1
        for i in range(0,len(self.mapa)):
                if not(i == wumppus.position[0]) and not (self.mapa[i][wumppus.position[1]].poco == 1) and not(self.mapa[i][wumppus.position[1]].wumppus == 1) and not(i == 0 and wumppus.position[1] == 0):
                    self.mapa[i][wumppus.position[1]].fedo = 1

        for i in range(0,len(self.mapa[wumppus.position[0]]))  :
                if not (i == wumppus.position[1]) and not(self.mapa[wumppus.position[0]][i].poco == 1) and not(self.mapa[wumppus.position[0]][i].wumppus == 1) and not(i == 0 and wumppus.position[0] == 0):
                    self.mapa[wumppus.position[0]][i].fedo = 1
       
    
    def criarPocos(self, wumppus):
        
        #o bloco a seguir e responsavel pela insercao dos pocos ao mapa com probalididade 0,2
        for i in range(0,len(self.mapa)):
            for j in range(0,len(self.mapa[i])):
                if(self.validarPosicao(i, j, wumppus)):
                    self.inserirPoco(j,i)
                    coordenadas =[i,j]
                    self.listaDePocos.append(coordenadas)
                if self.nPocos >= 3:
                    break
        
                



    def inserirPoco(self, x, y) : 
        print x, y
        #se o valor de  random deve estar entre 0 e 2  o poco sera criado
        if randrange(0,10) <= 2 :
            self.nPocos = self.nPocos + 1
            print "entrou if <= 2"
            self.mapa[y][x].poco = 1
            # adciona a briza de cada poco
            for i in range(0,len(self.mapa)):
                if not(i == y) and not (self.mapa[i][x].poco == 1) and not(self.mapa[i][x].wumppus == 1) and not(i == 0 and x == 0):
                    self.mapa[i][x].briza = 1

            for i in range(0,len(self.mapa[y]))  :
                if not (i == x) and not(self.mapa[y][i].poco == 1) and not(self.mapa[y][i].wumppus == 1) and not(i == 0 and y == 0):
                    self.mapa[y][i].briza = 1
                
                    
        

    

    def validarPosicao(self, i, j, wumppus):
        if i == wumppus.position[0] and j == wumppus.position[1]:
            return False
        if i == 0 or i == 1:
            if j > 2 :
               
                return True
            else:
                return False
        else:
            if j == 0 or j == 1:
                if i > 2:
                    return True
                else:
                    return False
            return True
        