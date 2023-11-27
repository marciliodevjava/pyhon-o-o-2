class Funcionario:

    def __init__(self, nome):
        self.__nome = nome

    def registra_horas(self, horas):
        print("Horas registradas")

    def mostrar_tarefas(self):
        print('Fez muita coisa')


class Alura(Funcionario):

    def __init__(self, nome):
        super().__init__(nome.title())

    @property
    def nome(self):
        return self._Funcionario__nome

    def mostrar_tarefas(self):
        return 'Fez muita coisa, Alurete'

    def buscar_perguntas_sem_resposta(self):
        return 'Mostrando perguntas não respondidas do forum'


class Caelum(Funcionario):

    def __init__(self, nome):
        super().__init__(nome.title())

    @property
    def nome(self):
        return self._Funcionario__nome

    def mostrar_tarefas(self):
        return 'Fez muita coisa, Calunete'

    def buscar_curso_do_mes(self, mes=None):
       return 'Mostrando cursos {}'.format(mes) if mes else 'Mostrando cursos desse mês'


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior('José')
luan = Pleno('Luan')
pedro = Pleno('Pedro')
joao = Senior('João')

print(f'Nome: {jose.nome}', jose.buscar_perguntas_sem_resposta())
print(f'Nome: {pedro.nome} ', pedro.buscar_curso_do_mes())
print(f'Nome: {luan.nome}', luan.mostrar_tarefas())
print(joao)
