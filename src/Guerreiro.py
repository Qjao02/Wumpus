from Mapa import Mapa

class Guerreiro:
    memoria = None
    flecha = None
    posicaoAtual = []
    posicaoSupostaWumppus = []
    posicaoSupostaOuro = None
    score = 0 
    supostaPosicaoPocos = None
    sensacoes = []


    def __init__(self):
        self.memoria = Mapa()
