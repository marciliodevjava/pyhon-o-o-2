class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()


class Filme (Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = float(duracao)

    def informacao(self):
        print("")
        print("Nome: {}".format(self._nome))
        print("Ano: {}".format(self._ano))
        print("Duração? {}".format(self._duracao))
        print("Likes: {}".format(self._likes))
        return ""

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def informacao(self):
        print("")
        print("Nome: {}".format(self._nome))
        print("Ano: {}".format(self._ano))
        print(f"Temporadas: {self._temporadas}")
        print("Likes: {}".format(self._likes))
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
