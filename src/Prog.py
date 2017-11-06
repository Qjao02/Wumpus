from Mapa import Mapa
from Wumppus import Wumppus
from Guerreiro import Guerreiro

def main():
    
    wumppus = Wumppus()
    mapa = Mapa()

     #cria o wumppus
    mapa.criarWumppus(wumppus)

    #cria os pocos
    mapa.criarPocos(wumppus)

    #seta o ouro
    mapa.inserirOuroEFlecha()
    
    mapa.printMapa()

    #debug
    for i in range(0,len(mapa.listaDePocos)):
        print mapa.listaDePocos[i]

    
    #cria Guerreiro
    guerreiro = Guerreiro()

    










if __name__ == '__main__':
    main()
    