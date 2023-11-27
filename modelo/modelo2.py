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

    def __str__(self):
        return "Nome: {} - Ano: {} - Likes: {}".format(self.__nome, self.__ano, self.__likes)


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = float(duracao)

    def __str__(self):
        super().__str__()
        return "Nome: {} - Ano: {} - Likes: {} - Duração: {}".format(super().nome, super().ano, super().likes, self._duracao)


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __str__(self):
        return "Nome: {} - Ano: {} - Likes: {} - Temporadas: {}".format(super().nome, super().ano, super().likes, self._temporadas)

class Playlist:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = list(programas)


    def __len__(self):
        return len(self.__programas)

    def list_programas(self):
        return self.__programas

    @property
    def listagem(self):
        return self.__programas

    def __getitem__(self, item):
        return self.__programas[item]

vingadores = Filme("Vingadores - Guerra Infinita", 2021, 2.35)
print(vingadores)
print('')
vingadores.dar_likes()
print(vingadores)
print('')

atlanta = Serie('Atlanta', 2018, 2)
print(atlanta)
print('')
atlanta.dar_likes()
print(atlanta)
print('')
atlanta.dar_likes()
print(atlanta)
print('')

tmep = Filme("Todo mundo em pânico", 1991, 100)
tmep.dar_likes()
demolidor = Serie("Demolidor", 2016, 2)
demolidor.dar_likes()
filme_e_serie = [vingadores, atlanta, tmep, demolidor]

for programa in filme_e_serie:
    programa
    print('')

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

print('')

playlist_fim_de_semana = Playlist('Fim de semana', filme_e_serie)

print(f'Tamanha da Playlist: {len(playlist_fim_de_semana)}')

for fds in playlist_fim_de_semana.list_programas():
    print(fds)

print('')

for fds in playlist_fim_de_semana:
    print(fds)

print('')

print(f'Tem a serie Demolidor: {demolidor in playlist_fim_de_semana.list_programas()}')
print(f'Tem a serie Vingadores: {vingadores in playlist_fim_de_semana}')
