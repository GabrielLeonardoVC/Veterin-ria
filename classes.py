class Pet:
    def __init__(self, nome, peso, raca, cor):
        self.__nome = nome
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor

    def emitir_som(self):
        raise NotImplementedError("Cada animal deve implementar seu próprio som.")
    
    def get_nome(self):
        return self.__nome
    
    def get_cor(self):
        return self.__cor
    
    def get_raca(self):
        return self.__raca
    
    def get_peso(self):
        return self.__peso

    def set_nome(self, nome):
        self.__nome = nome
    
    def set_cor(self, cor):
        self.__cor = cor
    
    def set_raca(self, raca):
        self.__raca = raca
    
    def set_peso(self, peso):
        self.__peso = peso

class Cachorro(Pet):
    def emitir_som(self):
        print("Auu Auu")

class Gato(Pet):
    def emitir_som(self):
        print("Miauu Miauu")

class Coelho(Pet):
    def emitir_som(self):
        print("Tchiki Tchiki")
