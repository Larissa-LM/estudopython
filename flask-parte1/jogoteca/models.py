class Jogo(): 
    def __init__(self, nome, categoria, console,id=None):
        self.nome = nome
        self.categoria = categoria 
        self.console = console
        self.id = id

class Usuario(): 
    def __init__(self, nome, id, senha):
        self.nome = nome 
        self.id = id
        self.senha = senha 