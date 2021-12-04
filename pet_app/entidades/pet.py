class Pet():
    def __init__(self, nome, idade, peso, categoria, cor, raca, genero, proprietario):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__categoria = categoria
        self.__cor = cor
        self.__raca = raca
        self.__genero = genero
        self.__proprietario = proprietario


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca
        
    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def proprietario(self):
        return self.__proprietario

    @proprietario.setter
    def proprietario(self, proprietario):
        self.__proprietario = proprietario

