class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = str(nome.title())
        self.__ano = int(ano)
        self.__duracao = float(duracao)
        self.__likes = int(0)

    def get_filme(self):
        nome = " Nome: {}".format(self.__nome)
        ano = " Ano: {}".format(self.__ano)
        duracao = " Duração: {}".format(self.__duracao)
        return nome + ano + duracao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    def dar_likes(self):
        self.__likes += 1

    def informacao(self):
        print("")
        print("Nome: {}".format(self.__nome))
        print("Ano: {}".format(self.__ano))
        print("Duração? {}".format(self.__duracao))
        print("Likes: {}".format(self.__likes))
        return ""

    @property
    def likes(self):
        return self.__likes()

    def dar_likes(self):
        self.__likes += 1

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = str(nome.title())
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = int(0)

    def contador_likes(self):
        self.__likes += 1

    def informacao(self):
        print("")
        print("Nome: {}".format(self.__nome))
        print("Ano: {}".format(self.__ano))
        print(f"Temporadas: {self.__temporadas}")
        print("Likes: {}".format(self.__likes))
        return ""


vingadores = Filme("Vingadores - Guerra Infinita", 2021, 2.35)
print(vingadores.nome)
print(vingadores.informacao())
vingadores.dar_likes()
vingadores.nome = "Vingadores - Guerra Infinita II"
print(vingadores.nome)
print(vingadores.informacao())


atlanta = Serie('Atlanta', 2018, 2)
print(atlanta.informacao())
atlanta.contador_likes()
print(atlanta.informacao())
atlanta.contador_likes()
print(atlanta.informacao())
