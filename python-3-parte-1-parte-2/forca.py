import random

def imprime_mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def cria_palavra_secreta(): 
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip() #Tirando o /n
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra): 
    return ["_" for letra in palavra] ##list comprehension 

def recebe_chute_do_jogador():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute

def marca_chute_correto(chute, letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def exibe_mensagem_ganhador(): 
    print("Parabéns, você venceu!!")

def exibe_mensagem_perdedor(): 
    print("Você perdeu!!")

def jogar():

    imprime_mensagem_de_abertura()

    palavra_secreta = cria_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0


    while (not acertou and not enforcou):

        chute = recebe_chute_do_jogador()
        

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            print("Você errou! Faltam {} tentativas".format(6 - tentativas))

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        exibe_mensagem_ganhador()
    else:
        exibe_mensagem_perdedor()


if(__name__ == "__main__"):
    jogar()