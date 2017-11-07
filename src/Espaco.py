class Espaco:
    wumppus = None
    ouro = None
    poco = None
    fedo = None
    briza = None
    visitado = 0

    def __init__(self):
        self.wumppus = 0
        self.dinheiro = 0
        self.flecha = 0
        self.fedo = 0
        self.briza = 0



    def mostrarEspaco(self):
        cont = 0
        listPrint = []
        if self.wumppus == 1:
            listPrint.append("wumppus")
            cont = 1
        if self.ouro == 1:
            listPrint.append("resplendor")
            cont = 1
        if self.flecha == 1:
            listPrint.append("flecha")
            cont = 1
        if self.fedo == 1:
            listPrint.append("fedo")
            cont = 1
        if self.briza == 1:
            listPrint.append("briza")
            cont = 1
        if self.poco == 1:
            listPrint.append("poco")
            cont = 1
        
        if cont == 0:
            listPrint.append("vazio")
        
        listPrint.append(' |||||||||')
        print listPrint



