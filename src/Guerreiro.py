from Mapa import Mapa

class Guerreiro:
    memoria = None
    flecha = None
    posicaoAtual = None
    posicaoSupostaWumppus = []
    posicaoSupostaOuro = None
    score = 0 
    supostaPosicaoPocos = None
    sensacoes = []


    def __init__(self):

        self.memoria = Mapa()
        self.posicaoAtual = [0,0]



    def sentir(self,listaSensacao):
        pass



