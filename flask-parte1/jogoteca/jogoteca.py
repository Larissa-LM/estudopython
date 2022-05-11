from flask import Flask, render_template

class Jogo(): 
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria 
        self.console = console


app = Flask(__name__) # __name__ faz referência ao próprio arquivo e garante que vai rodar a aplicação

@app.route('/inicio') #para colocar uma informação no site precisamos colocar uma rota e em seguida precisamos criar uma função para definir o que existe dentro dessa rota
def ola():
    jogo1 = Jogo("Tetris", "Puzzle" , "Atari")
    jogo2 = Jogo("God of War","Rack n Slash", "PS2" )
    jogo3 = Jogo("Mortal Kombat", "Luta", "PS2")
    lista_de_jogos = [jogo1, jogo2, jogo3]
    return render_template("lista.html", titulo = "Jogos", jogos = lista_de_jogos) # Não é uma boa prática utilizar o html direto e sim importá-lo. render_tempĺate sabe que existe uma pasta templates então é só passar o arquivo
                                                           # Além disso é posssível passar variáveis daqui para o arquivo html através do render 
    
    #return "<h1>Olá mundo</h1>" Precisamos colocar tags html por estar trabalhando com web 

app.run() #para conseguir rodar a aplicação 