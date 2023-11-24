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
    
    def informacao(self):
        print("Nome: {}".format(self.__nome))
        print("Ano: {}".format(self.__ano))
        print("Likes: {}".format(self.__likes))
        
class Filme (Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = float(duracao)

    def informacao(self):
        super().informacao()
        print("Duração: {}".format(self._duracao))
        return ""

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def informacao(self):
        super().informacao()
        print("Temporadas: {}".format(self._temporadas))
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


filme_e_serie = [vingadores, atlanta]

for programa in filme_e_serie:
    print(programa.informacao())

# Utilizando hasattr
for programa in filme_e_serie:
    detalhes = programa._duracao if hasattr(programa, '_duracao') else programa._temporadas
    print(f'Nome: {programa.nome} - Ano: {programa.ano} - {detalhes} - Likes: {programa.likes}')
    print('')

# Utilizando hasattr
for programa in filme_e_serie:
    nome = ''
    detalhe = ''
    if hasattr(programa, "_duracao"):
        nome = 'Duração:'
        detalhe = programa._duracao

    if hasattr(programa, '_temporadas'):
        nome = 'Temporadas:'
        detalhe = programa._temporadas

    print(f'Nome: {programa.nome} - Ano: {programa.ano} - {nome} {detalhe} - Likes: {programa.likes}')
