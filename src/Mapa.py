from random import *

class Mapa :
    mapa = []
    pocos = 0


    def __init__ (self,wumppus):
        
        list1 = [0,0,0,0]
        list2 = [0,0,0,0]
        list3 = [0,0,0,0]
        list4 = [0,0,0,0]

        self.mapa.append(list1)
        self.mapa.append(list2)
        self.mapa.append(list3)
        self.mapa.append(list4)  
        
        self.criarWumppus(wumppus)




    def criarWumppus(self, wumppus):
        
        self.mapa[wumppus.position[0]][wumppus.position[1]] = "wumppus"
        print wumppus.position
    
    def criarPocos(self):
    
        for i in range(0,len(self.mapa)):
            for j in range(0,len(self.mapa[i])):
                inserirPoco(j,i)
                if self.pocos >= 3:
                    break
                



    def inserirPoco(self, x, y) : 
        if randrange(0,10) <= 2 :
            self.mapa[x][y] = "poco"
            for i in range(0,len(self.mapa)):
                if i 
        

    def printMapa(self):
         
         for i in range(0,len(self.mapa)):
            print self.mapa[i]