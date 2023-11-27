class Funcionario:

    def registra_horas(self, horas):
        print("Horas registradas")

    def mostrar_tarefas(self):
        print('Fez muita coisa')


class Alura(Funcionario):

    def __init__(self, nome):
        self.__nome = str(nome.title())

    def nome(self):
        return self.__nome

    def mostrar_tarefas(self):
        return 'Fez muita coisa, Alurete'

    def buscar_perguntas_sem_resposta(self):
        return 'Mostrando perguntas não respondidas do forum'


class Caelum(Funcionario):

    def __init__(self, nome):
        self.__nome = str(nome.title())

    def nome(self):
        return self.__nome

    def mostrar_tarefas(self):
        return 'Fez muita coisa, Calunete'

    def buscar_curso_do_mes(self, mes=None):
       return 'Mostrando cursos {}'.format(mes) if mes else 'Mostrando cursos desses mês'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


jose = Junior('José')
luan = Pleno('Luan')
pedro = Pleno('Pedro')

print(f'Nome: {jose.nome()} ', jose.buscar_perguntas_sem_resposta())
print(f'Nome: {pedro.nome()} ', pedro.buscar_curso_do_mes())
print(f'Nome: {luan.nome()}', luan.mostrar_tarefas())
