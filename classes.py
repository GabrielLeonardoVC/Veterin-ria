class Cachorro:
    def __init__(self, nome, peso, raca, cor, idade):
        self.__nome = nome
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__idade = idade
        self.__especie = "Cachorro"
    def getNome(self): return self.__nome
    def getCor(self): return self.__cor
    def getRaca(self): return self.__raca
    def getPeso(self): return self.__peso
    def getIdade(self): return self.__idade
    def getEspecie(self): return self.__especie

    def setNome(self, nome): self.__nome = nome
    def setPeso(self, peso): self.__peso = peso
    def setRaca(self, raca): self.__raca = raca
    def setCor(self, cor): self.__cor = cor
    def setIdade(self, idade): self.__idade = idade

class Gato:
    def __init__(self, nome, peso, raca, cor, idade):
        self.__nome = nome
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__idade = idade
        self.__especie = "Gato"

    def getNome(self): return self.__nome
    def getCor(self): return self.__cor
    def getRaca(self): return self.__raca
    def getPeso(self): return self.__peso
    def getIdade(self): return self.__idade
    def getEspecie(self): return self.__especie
    def setNome(self, nome): self.__nome = nome
    def setPeso(self, peso): self.__peso = peso
    def setRaca(self, raca): self.__raca = raca
    def setCor(self, cor): self.__cor = cor
    def setIdade(self, idade): self.__idade = idade

class Passaro:
    def __init__(self, nome, peso, raca, cor, idade):
        self.__nome = nome
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__idade = idade
        self.__especie = "Passaro"

    def getNome(self): return self.__nome
    def getCor(self): return self.__cor
    def getRaca(self): return self.__raca
    def getPeso(self): return self.__peso
    def getIdade(self): return self.__idade
    def getEspecie(self): return self.__especie

    def setNome(self, nome): self.__nome = nome
    def setPeso(self, peso): self.__peso = peso
    def setRaca(self, raca): self.__raca = raca
    def setCor(self, cor): self.__cor = cor
    def setIdade(self, idade): self.__idade = idade
