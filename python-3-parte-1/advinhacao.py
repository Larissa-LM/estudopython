import random

print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1

for rodada in range(1,total_de_tentativas + 1): 
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100: ") # Aqui recebe uma string "42" precisa converter
    numero_chutado = int(chute) #conversão

    print("Você digitou" , chute)

    if(numero_chutado < 1 or numero_chutado > 100):
        print("Você deve digitar um número entre 1 e 100 \n")
        continue

    acertou = numero_chutado == numero_secreto

    if(acertou):
        print("Você acertou!!")
        break
    else:
        if(numero_chutado > numero_secreto):
            print("Você errou!! O seu chute foi maior que o número secreto")
        elif(numero_chutado < numero_secreto):
            print("Você errou!! O seu chute foi menor que o número secreto")

    print("Fim do jogo")
