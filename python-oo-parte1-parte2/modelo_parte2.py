class Programa: 
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano 
        self._likes = 0 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self): 
        return self._likes

    def dar_like(self):
        self._likes += 1


class Filme(Programa): #Herdando da classe Programa

    def __init__(self, nome, ano, duracao):
        #self._nome = nome.title()
        #self.ano = ano 
        #self._likes = 0 Para evitar repetição de código, existe outra maneira de usar atributos da classe mãe:

        super().__init__(nome,ano)
        self.duracao = duracao


class Serie(Programa): 

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
        
    


vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
vingadores.dar_like()

print(f'Nome: {vingadores._nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes:{vingadores.likes} ')

mordern_family = Serie("modern family", 2009, 11)
mordern_family.dar_like()

print(f'Nome: {mordern_family._nome} - Ano: {mordern_family.ano} - Temporadas: {mordern_family.temporadas} - Likes:{mordern_family.likes}')

filmes_e_series = [vingadores,mordern_family]

for programa in filmes_e_series: 
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas # hasattr é utilizado para verificar se um atributo existe em uma classe (existe duracaqo dentro do objeto programa?)
    print(f'{programa.nome} - {detalhes}  - {programa.likes}')


    
        