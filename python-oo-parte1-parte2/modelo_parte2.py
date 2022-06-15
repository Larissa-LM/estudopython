class Programa: 
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano 
        self._likes = 0 #atributo protegido 

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
    
    def __str__(self): # Dunder method que transforma o retorno em string 
        return (f'{self._nome} - {self.ano} - {self._likes} likes')

class Filme(Programa): #Herdando da classe Programa

    def __init__(self, nome, ano, duracao):
        #self._nome = nome.title()
        #self.ano = ano 
        #self._likes = 0 Para evitar repetição de código, existe outra maneira de usar atributos da classe mãe:

        super().__init__(nome,ano) #super() chama qualquer atributo da classe mãe
        self.duracao = duracao
    
    def __str__(self): 
        return (f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes')

class Serie(Programa): 

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    
    def __str__(self): 
        return(f'{self._nome} - {self.ano} - {self.temporadas} temporada(s) - {self._likes} likes')

class Playlist: 

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas= programas

    def __getitem__(self, item): #Método que indica que classe pode ser usada para for in ou in (iterável) conhecido como duck type
        return self._programas[item]
         
    def __len__(self): # Dunder method que implementa o comportamento de sized uma ideia de algo que possui tamanho, e que então precisará implementar um __len__() para que o len() externo possa funcionar em nossa classe.
        return len(self._programas)

    #@property
    #def listagem(self):
        #return self._programas
    
    #@property
    #def tamanho(self):
        #return len(self.programas)

     
vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
vingadores.dar_like()

coracao_marcado = Serie("Coração Marcado", 2022, 1)
coracao_marcado.dar_like() 

emily_in_paris = Serie("Emily in Paris", 2021, 2)
emily_in_paris.dar_like()

mordern_family = Serie("modern family", 2009, 11)
mordern_family.dar_like()

filmes_e_series = [vingadores,mordern_family, coracao_marcado, emily_in_paris]
playlist_fim_de_semana = Playlist("Playlist fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}') # sempre que o len() externo for chamado, conseguiremos obter o __len__() da nossa listagem interna.


for programa in playlist_fim_de_semana: 
    #detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas # hasattr é utilizado para verificar se um atributo existe em uma classe (existe duracaqo dentro do objeto programa?)
    #Reduzindo if
    print(programa)

print(f'Existe ou não? {emily_in_paris in playlist_fim_de_semana}') #__getitem__ permite utilizar o in para saber se o item está ou não contido na lista

print(f'Pegando primeiro item da lista: {playlist_fim_de_semana[0]}') # __getitem__ permite pegar itens por index
    
        