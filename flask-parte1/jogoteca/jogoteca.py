from flask import Flask, render_template

app = Flask(__name__) # __name__ faz referência ao próprio arquivo e garante que vai rodar a aplicação

@app.route('/inicio') #para colocar uma informação no site precisamos colocar uma rota e em seguida precisamos criar uma função para definir o que existe dentro dessa rota
def ola():
    return render_template("lista.html") # Não é uma boa prática utilizar o html direto e sim importá-lo. render_tempĺate sabe que existe uma pasta templates então é só passar o arquivo
    
    #return "<h1>Olá mundo</h1>" Precisamos colocar tags html por estar trabalhando com web 

app.run() #para conseguir rodar a aplicação 