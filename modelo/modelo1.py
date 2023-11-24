class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def ano(self):
        return self.__ano
class Filme (Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = float(duracao)

    def informacao(self):
        print("")
        print("Nome: {}".format(super().nome))
        print("Ano: {}".format(super().ano))
        print("Duração? {}".format(self._duracao))
        print("Likes: {}".format(super().likes))
        return ""

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def informacao(self):
        print("")
        print("Nome: {}".format(super().nome))
        print("Ano: {}".format(super().ano))
        print(f"Temporadas: {self._temporadas}")
        print("Likes: {}".format(super().likes))
        return ""


vingadores = Filme("Vingadores - Guerra Infinita", 2021, 2.35)
print(vingadores.informacao())
vingadores.dar_likes()
print(vingadores.informacao())

atlanta = Serie('Atlanta', 2018, 2)
print(atlanta.informacao())
atlanta.dar_likes()
print(atlanta.informacao())
atlanta.dar_likes()
print(atlanta.informacao())
