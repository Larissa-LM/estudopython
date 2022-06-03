import os


SECRET_KEY = "luna" # por estarmos guardando as informações no navegador(nos cookies) precisamos de uma secret key para evitar que pessoas mal intecionadas acesse a aplicação e faça alterações
MYSQL_HOST = "0.0.0.0"
MYSQL_USER = "root"
MYSQL_PASSWORD = "admin"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads' #Passando o caminho absoluto, onde dirname poega desde da raiz do diretório e o abspath pega o file jogoteca.py
