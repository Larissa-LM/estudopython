def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] ##list comprehension 

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Você errou! Faltam {} tentativas".format(6 - tentativas))

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()