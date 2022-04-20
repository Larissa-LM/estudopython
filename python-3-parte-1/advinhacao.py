print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas ): 
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu número: ") # Aqui recebe uma string "42" precisa converter
    numero_chutado = int(chute) #conversão

    print("Você digitou" , chute)

    acertou = numero_chutado == numero_secreto

    if(acertou):
        print("Você acertou!!")
    else:
        if(numero_chutado > numero_secreto):
            print("Você errou!! O seu chute foi maior que o número secreto")
        elif(numero_chutado < numero_secreto):
            print("Você errou!! O seu chute foi menor que o número secreto")

    rodada = rodada + 1 

    print("Fim do jogo")
