class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster(Funcionario): #Mixin: classes pequenas que não possuem objetos instanciados
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum,Hipster):
    pass 


luna = Junior("Luna")
marie = Pleno("Marie")

luna.busca_perguntas_sem_resposta()

marie.busca_cursos_do_mes()

berfin = Senior("Berfin")
print(berfin)


#Algoritmo MRO 

#pleno > Alura > Funcionário > Caelum > Funcionário
# em caso de repetições se a classe for uma good head, ou seja não tenho nenhuma outra classe que é da mesma hierarquia que fuuncionário(que está abaixo de funcionário)
# se existe uma outra classe que herda de funcionário o fluxo muda, tornando: 
# pleno > Alura  > Caelum > Funcionário então Caelum é uma good head

