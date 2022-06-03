import os
from jogoteca import app 

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']): # percorrendo os nomes dos arquivos direto na pasta. Obs: listdir() permite que percorra os nomes dos arquivos diretamente no diretório
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

def deleta_imagem(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'],arquivo)) #removendo a imagem. join permite juntar diferentes paths, neste caso o app.config['UPLOAD_PATH'] e o arquivo.
