from random import *

class Wumppus :
    
    estado = None
    position = []


    def __init__ (self):
        
        self.position.append(randrange(0,4))
        self.position.append(randrange(0,4))
        while not(self.validarPosicao()):
            self.position.append(randrange(0,4))
            self.position.append(randrange(0,4))
            self.validarPosicao()
        
        self.estado = "vivo"


    def validarPosicao(self):

        if self.position[0] == 0 or self.position[0] == 1:
            if self.position > 2 :
                return True
            else:
                return False
        else:
            return True