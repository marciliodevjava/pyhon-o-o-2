class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = str(nome.title())
        self.__ano = int(ano)
        self.__duracao = float(duracao)

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
        self.__nome = nome

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = str(nome.title())
        self.__ano = ano
        self.__temporadas = temporadas


    def informacao(self):
        print("")
        print("Nome: {}".format(self.__nome))
        print("Ano: {}".format(self.__ano))
        print(f"Temporadas: {self.__temporadas}")
        return ""


vingadores = Filme("Vingadores - Guerra Infinita", 2021, 2.35)
print(vingadores.nome)
vingadores.nome = "Vingadores - Guerra Infinita II"
print(vingadores.nome)


atlanta = Serie('Atlanta', 2018, 2)
print(atlanta.informacao())
