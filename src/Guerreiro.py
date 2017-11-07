from Mapa import Mapa

class Guerreiro:
    memoria = None
    flecha = 1
    posicaoAtual = None
    posicaoSupostaWumppus = []
    posicaoSupostaOuro = None
    score = 0 
    supostaPosicaoPocos = None
    sensacoes = None


    def __init__(self):

        self.memoria = Mapa()
        self.posicaoAtual = [0,0]



    def agir(self, listaSensacoes):
        self.sensacoes = listaSensacoes
        self.copiaParaMemoria




    def copiaParaMemoria (self):
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].wumppus = listaSensacoes.wumppus
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].ouro = listaSensacoes.ouro
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].fedo = listaSensacoes.fedo
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].briza = listaSensacoes.briza
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].poco = listaSensacoes.poco



    #movimentoDoJogador
    def moveUp(self):
        pass
        
    def moveUp(self):
        pass

    def moveUp(self):
        pass

    def moveUp(self):
        pass

    def AtirarFlecha(self):
        pass

    def pegarOuro(self):
        pass


    def gerarPossibilidades(self):
        pass