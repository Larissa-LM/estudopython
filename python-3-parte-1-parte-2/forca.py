
def jogar():
    print("*******************************")
    print("Bem-vindo ao jogo de Forca")
    print("*******************************")

    palavra_secreta = "banana".upper()
    enforcou = False
    acertou = False
    letras_acertadas = ["_","_","_","_","_","_" ]
    tentativas = 0 

    print(letras_acertadas)

    while(not acertou and not enforcou):
        
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:

                if(chute == letra):

                    letras_acertadas[index] = letra 

                    index = index + 1 
        else: 
            tentativas += 1

        print(letras_acertadas)

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você errou!!!")
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
