import random

def jogar():
    print("*******************************")
    print("Bem-vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade? \n")
    print("(1) Fácil (2) Médio (3) Difícil \n")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 5
    elif(nivel == 2):
        total_de_tentativas = 3
    else: 
        total_de_tentativas = 2

    for rodada in range(1,total_de_tentativas + 1): 
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ") # Aqui recebe uma string "42" precisa converter
        numero_chutado = int(chute) #conversão

        print("Você digitou\n" , chute)

        if(numero_chutado < 1 or numero_chutado > 100):
            print("Você deve digitar um número entre 1 e 100 \n")
            continue

        acertou = numero_chutado == numero_secreto
        maior = numero_chutado > numero_secreto
        menor = numero_chutado < numero_secreto

        if(acertou):
            print("Você acertou!!Total de pontos {}\n".format(pontos))
            break
        else:
            if(maior):
                print("Você errou!! O seu chute foi maior que o número secreto\n")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}\n".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou!! O seu chute foi menor que o número secreto\n")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}\n".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - numero_chutado) # 20 - 10 = 10 abs() deixa o resultado positivo
            pontos = pontos - pontos_perdidos 

        print("Fim do jogo")
