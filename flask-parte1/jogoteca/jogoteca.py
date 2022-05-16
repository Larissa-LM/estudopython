
from distutils.log import debug
from flask import Flask, render_template, request, redirect, session, flash

class Jogo(): 
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria 
        self.console = console


app = Flask(__name__) # __name__ faz referência ao próprio arquivo e garante que vai rodar a aplicação
app.secret_key = "luna" # por estarmos guardando as informações no navegador(nos cookies) precisamos de uma secret key para evitar que pessoas mal intecionadas acesse a aplicação e faça alterações

jogo1 = Jogo("Tetris", "Puzzle" , "Atari")
jogo2 = Jogo("God of War","Rack n Slash", "PS2" )
jogo3 = Jogo("Mortal Kombat", "Luta", "PS2")
lista_de_jogos = [jogo1, jogo2, jogo3]


@app.route('/') #para colocar uma informação no site precisamos colocar uma rota e em seguida precisamos criar uma função para definir o que existe dentro dessa rota
def index():
    return render_template("lista.html", titulo = "Jogos", jogos = lista_de_jogos) # Não é uma boa prática utilizar o html direto e sim importá-lo. render_tempĺate sabe que existe uma pasta templates então é só passar o arquivo
                                                           # Além disso é posssível passar variáveis daqui para o arquivo html através do render 
    
    #return "<h1>Olá mundo</h1>" Precisamos colocar tags html por estar trabalhando com web 

@app.route("/novojogo") #nova página com um forms para adicionar um novo jogo
def adicionar_novo_jogo():
    if "usuario_logado" not in session or session["usuario_logado"] == None: 
        return redirect("/login")
    else: 
        return render_template("novo_jogo.html", titulo = "Novo Jogo") 

@app.route("/criar-novo-jogo", methods = ["POST" ,]) #Rota intermediária
def criar_novo_jogo(): 
    nome = request.form["nome"] #request é um helper do flask que captura a informação do form neste caso. Passamos os valores da tag name do arquivo no_jogo.html nos [""]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome,categoria,console)
    lista_de_jogos.append(jogo)
    
    return redirect("/") #redirecionando para a página inicial

@app.route("/login")
def login(): 
    return render_template("login.html")

@app.route("/autenticar", methods = ["POST"])
def autenticar(): 
    if "distrito12" == request.form["senha"]:
        session["usuario_logado"] = request.form["usuario"]
        flash(session["usuario_logado"] + " logado com sucesso!")
        return redirect("/")
    else:
        flash("Usuário não logado!")
        return redirect("/login")

@app.route("/logout")
def logout(): 
    session["usuario_logado"] = None 
    flash("Logout realizado com sucesso!")
    return redirect("/")

app.run(debug=True) #para conseguir rodar a aplicação 