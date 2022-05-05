from select import select


class Filme: 

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano 
        self.duracao = duracao
        self.__likes = 0 

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self,novo_nome):
        self.nome = novo_nome.title()

    @property
    def likes(self): 
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    def dar_like(self):
        self.likes += 1


class Serie: 

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano 
        self.temporadas = temporadas
        self.__likes = 0 
    
    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self,novo_nome):
        self.nome = novo_nome.title()

    @property
    def likes(self): 
        return self.__likes

    def dar_like(self):
        self.__likes += 1


vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes:{vingadores.like} ')

mordern_family = Serie("modern family", 2009, 11)
mordern_family.dar_like()

print(f'Nome: {mordern_family.nome} - Ano: {mordern_family.ano} - Temporadas: {mordern_family.temporadas} - Likes:{mordern_family.like}')


    
        