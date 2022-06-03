from distutils.log import debug
from flask import Flask 
from flask_mysqldb import MySQL

app = Flask(__name__) # __name__ faz referência ao próprio arquivo e garante que vai rodar a aplicação/ app sendo criada
app.config.from_pyfile('config.py')

db = MySQL(app)

from views import * # * importar todas as rotas

if __name__ == '__main__':
    app.run(debug=True) #para conseguir rodar a aplicação 

