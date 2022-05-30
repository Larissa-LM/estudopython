
from distutils.log import debug
from flask import Flask, render_template, request, redirect, session, flash, url_for

from flask_mysqldb import MySQL 
from dao import JogoDao, UsuarioDao
from models import Jogo, Usuario
import os




app = Flask(__name__) # __name__ faz referência ao próprio arquivo e garante que vai rodar a aplicação
app.secret_key = "luna" # por estarmos guardando as informações no navegador(nos cookies) precisamos de uma secret key para evitar que pessoas mal intecionadas acesse a aplicação e faça alterações
app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads' #Passando o caminho absoluto, onde dirname poega desde da raiz do diretório e o abspath pega o file jogoteca.py

db = MySQL(app)
jogo_dao = JogoDao(db)

usuario_dao = UsuarioDao(db)


 @app.route('/') #para colocar uma informação no site precisamos colocar uma rota e em seguida precisamos criar uma função para definir o que existe dentro dessa rota
def index():
    lista_de_jogos = jogo_dao.listar()
    return render_template("lista.html", titulo = "Jogos", jogos = lista_de_jogos) # Não é uma boa prática utilizar o html direto e sim importá-lo. render_tempĺate sabe que existe uma pasta templates então é só passar o arquivo
                                                           # Além disso é posssível passar variáveis daqui para o arquivo html através do render 
    
    #return "<h1>Olá mundo</h1>" Precisamos colocar tags html por estar trabalhando com web 

@app.route("/adicionar_novo_jogo") #nova página com um forms para adicionar um novo jogo
def adicionar_novo_jogo():
    if "usuario_logado" not in session or session["usuario_logado"] == None: 
        return redirect(url_for("login", proxima = url_for("adicionar_novo_jogo"))) #url dinâmica
                #(/login?proxima=criar-novo-jogo) é uma query string onde crio uma variável para indicar a página que quero se redirecionada
    else:
        return render_template("novo_jogo.html", titulo = "Novo Jogo") 

@app.route("/criar-novo-jogo", methods = ["POST" ,]) #Rota intermediária
def criar_novo_jogo(): 
    nome = request.form["nome"] #request é um helper do flask que captura a informação do form neste caso. Passamos os valores da tag name do arquivo no_jogo.html nos [""]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome,categoria,console)
    jogo = jogo_dao.salvar(jogo)
    imagem = request.files["imagem"]
    imagem.save(f'{}/{imagem.filename}')
    upload_path = app.config['UPLOAD_PATH']
    imagem.save(f'{upload_path}/capa{jogo.id},jpg') # salvando o nome do arquivo com o id do jogo
    #imagem.save(f'uploads/{imagem.filename}') Caminho para a imagem chumbado
    
    return redirect(url_for("index")) #redirecionando para a página inicial

@app.route("/editar/<int:id>") #para passar parâmetros em uma rota utilizamos os <> 
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id = id)))
    jogo = jogo_dao.busca_por_id(id)
    return render_template('editar.html', titulo = 'Editando jogo', jogo = jogo)


@app.route("/atualizar", methods = ["POST" ,]) #Rota intermediária
def atualizar(): 
    nome = request.form["nome"] 
    categoria = request.form["categoria"]
    console = request.form["console"]
    id = request.form["id"]
    jogo = Jogo(nome,categoria,console, id) 
    jogo_dao.salvar(jogo)
    
    return redirect(url_for("index")) 

@app.route("/deletar/<int:id>")
def deletar(id):
    jogo_dao.deletar(id)
    flash("Jogo removido com sucesso!")
    return redirect(url_for("index"))

@app.route("/login")
def login(): 
    proxima = request.args.get("proxima") # variavel proxima captura a informação da query string criada em adicionar_novo_jogo
    return render_template("login.html", proxima = proxima) # aqui estamos informando a próxima página pra o html do login 

@app.route("/autenticar", methods = ["POST"])
def autenticar():
    #import pdb
    #pdb.set_trace()
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.id
            flash(usuario.id + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']

            return redirect(proxima_pagina)
    

    flash("Usuário não logado!")
    return redirect(url_for("login"))

@app.route("/logout")
def logout(): 
    session["usuario_logado"] = None 
    flash("Logout realizado com sucesso!")
    return redirect(url_for("index"))

app.run(debug=True) #para conseguir rodar a aplicação 