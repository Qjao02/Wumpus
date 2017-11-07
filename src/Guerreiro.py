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
        self.atualizaConhecimento()





    def copiaParaMemoria (self):
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].wumppus = listaSensacoes.wumppus
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].ouro = listaSensacoes.ouro
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].fedo = listaSensacoes.fedo
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].briza = listaSensacoes.briza
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].poco = listaSensacoes.poco
        self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].visitado = 1



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


    def atualizaConhecimento(self):

       self.atualizaAdjPersonagem()


    def atualizaAdjPersonagem(self):

        if self.posicaoAtual[0] - 1 > = 0 :
            if self.memoria[0 - 1].visitado == 0:

                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].briza == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].poco = 1
                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].fedo == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].wumppus = 1


        if self.posicaoAtual[0] + 1 < 4 :
            if self.memoria[0 + 1].visitado == 0:

                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].briza == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].poco = 1
                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].fedo == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].wumppus = 1


        if self.posicaoAtual[1] - 1 > = 0 :
            if self.memoria[0 - 1].visitado == 0:

                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].briza == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].poco = 1
                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].fedo == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].wumppus = 1


        if self.posicaoAtual[1] + 1 < 4 :
            if self.memoria[0 - 1].visitado == 0:

                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].briza == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].poco = 1
                if self.memoria[self.posicaoAtual[0]][self.posicaoAtual[1]].fedo == 1:
                    self.memoria[0 - 1][self.posicaoAtual[1]].wumppus = 1



                
   
                