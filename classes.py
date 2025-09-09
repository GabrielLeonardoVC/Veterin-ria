class Clinica:
    def __init__(self, nome, cidade):
        self.__nome = nome
        self.__cidade = cidade
        self.__pets = {}
    
    def cadastroCachorro(self, nome, peso, raca, cor):
        self.__pets[len(self.__pets) + 1] = Cachorro(nome=nome, peso=peso, raca=raca, cor=cor)

    def cadastroGato(self, nome, peso, raca, cor):
        self.__pets[len(self.__pets) + 1] = Gato(nome=nome, peso=peso, raca=raca, cor=cor)

    def cadastroCoelho(self, nome, peso, raca, cor):
        self.__pets[len(self.__pets) + 1] = Coelho(nome=nome, peso=peso, raca=raca, cor=cor)

    def listar(self):
        return self.__pets
    
    def alterarNome(self, id, nome):
        self.__pets[id].setNome(nome)

    def alterarPeso(self, id, peso):
        self.__pets[id].setPeso(peso)

    def alterarCor(self, id, cor):
        self.__pets[id].setCor(cor)

    def alterarRaca(self, id, raca):
        self.__pets[id].setRaca(raca)

class Animal:
    def __init__(self, nome, peso, raca, cor):
        self.__nome = nome
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
    
    # ----------------- -------------------------
    #Metodos GETs && SETs

    def getNome(self):
        return self.__nome
    
    def getCor(self):
        return self.__cor
    
    def getRaca(self):
        return self.__raca
    
    def getPeso(self):
        return self.__peso
    
    #-------------------------------------------

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome
    
    def setCor(self, cor):
        self.__cor = cor
        return self.__cor
    
    def setRaca(self, raca):
        self.__raca = raca
        return self.__raca

    def setPeso(self, peso):
        self.__peso = peso
        return self.__peso

class Cachorro(Animal):
       
    # ----------------- -------------------------
    #Metodos

    def latir(self):
        return "Au Au"  
    

class Gato(Animal):    
    # ----------------- -------------------------
    #Metodos

    def miar(self):
        return "Miau Miau"
    

class Coelho(Animal):   
    # ----------------- -------------------------
    #Metodos

    def chiar(self):
        return "Chi Chi"