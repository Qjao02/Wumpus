from random import *
from Espaco import Espaco

class Mapa :
    mapa = []
    nPocos = 0
    listaDePocos = []


    def __init__ (self):
        
        #criaMatriz
        for i in range (0,4):
            newList = []
            for j in range(0,4):
                newEspaco = Espaco()
                newList.append(newEspaco)
            self.mapa.append(newList)        
       
        

    def printMapa(self):

        print "blabla"
        listPrint = []
        cont = 0
        for i in range(0,len(self.mapa)):
            cont = 0
            for j in range(0, len(self.mapa[i])):
                cont = 0
                listPrint.append('|||||||| ')
                if self.mapa[i][j].wumppus == 1:
                    listPrint.append("wumppus")
                    cont = 1
                if self.mapa[i][j].ouro == 1:
                    listPrint.append("resplendor")
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
                
                listPrint.append(' |||||||||')
            print listPrint
            listPrint[:] = []
    
    def criarWumppus(self, wumppus):
        
        #adcionaWumppus ao mapa
        self.mapa[wumppus.position[0]][wumppus.position[1]].wumppus = 1
        for i in range(0,len(self.mapa)):
                if not(i == wumppus.position[0]) and not (self.mapa[i][wumppus.position[1]].poco == 1) and not(self.mapa[i][wumppus.position[1]].wumppus == 1) and not(i == 0 and wumppus.position[1] == 0) and ((i == wumppus.position[0] - 1) or (i == wumppus.position[0] + 1)):
                    self.mapa[i][wumppus.position[1]].fedo = 1

        for i in range(0,len(self.mapa[wumppus.position[0]]))  :
                if not (i == wumppus.position[1]) and not(self.mapa[wumppus.position[0]][i].poco == 1) and not(self.mapa[wumppus.position[0]][i].wumppus == 1) and not(i == 0 and wumppus.position[0] == 0) and ((i == wumppus.position[1] - 1) or (i  == wumppus.position[1] + 1)):
                    self.mapa[wumppus.position[0]][i].fedo = 1

        self.printMapa()
       
    
    def criarPocos(self, wumppus):
        
        #o bloco a seguir e responsavel pela insercao dos pocos ao mapa com probalididade 0,2
        for i in range(0,len(self.mapa)):
            for j in range(0,len(self.mapa[i])):
                if(self.validarPosicao(i, j, wumppus)):
                    self.inserirPoco(j,i)
                if self.nPocos >= 3:
                    break
        

        self.printMapa()

        
                



    def inserirPoco(self, x, y) : 

        #se o valor de  random deve estar entre 0 e 2  o poco sera criado
        if randrange(0,10) <= 2 :

            self.nPocos = self.nPocos + 1
            print "poco selecionado"
            self.mapa[y][x].poco = 1
            coordenadas = [y,x]
            self.listaDePocos.append(coordenadas)

            # adciona a briza de cada poco
            for i in range(0,len(self.mapa)):
                if not(i == y) and not (self.mapa[i][x].poco == 1) and not(self.mapa[i][x].wumppus == 1) and not(i == 0 and x == 0) and ((i == y-1) or (i == y + 1)):
                    self.mapa[i][x].briza = 1

            for i in range(0,len(self.mapa[y]))  :
                if not (i == x) and not(self.mapa[y][i].poco == 1) and not(self.mapa[y][i].wumppus == 1) and not(i == 0 and y == 0) and ((i == x - 1) or (i == x + 1)):
                    self.mapa[y][i].briza = 1
                
        self.printMapa()
                    
        

    

    def validarPosicao(self, i, j, wumppus):
        
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

    def validarPosicaoOuro(self, i, j):
        for a in range(0,len(self.listaDePocos)):
            if i == self.listaDePocos[a][0] and j == self.listaDePocos[a][1]:
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
    
    def inserirOuro(self):
        
        x = randrange(0,4)
        y = randrange(0,4)
        while not(self.validarPosicaoOuro(y,x)):
            x = randrange(0,4)
            y = randrange(0,4) 
        self.mapa[y][x].ouro = 1



    def pegarSensacao(self,guerreiro):

        sensacoes = self.mapa[guerreiro.posicaoAtual[0]][guerreiro.posicaoAtual[1]]
        sensacoes.mostrarEspaco() 

        return sensacoes
