class Filme: 

    def __init__(self, nome, ano, duracao):
        self.nome = nome 
        self.ano = ano 
        self.duracao = duracao


class Serie: 

    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano 
        self.temporadas = temporadas


vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')

mordern_family = Serie("Modern Family", 2009, 11)
print(f'Nome: {mordern_family.nome} - Ano: {mordern_family.ano} - Temporadas: {mordern_family.temporadas}')


    
        