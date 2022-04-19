print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = 42
 
chute = input("Digite o seu número: ") # Aqui recebe uma string "42" precisa converter
numero_chutado = int(chute) #conversão 

print("Você digitou" , chute)

if(numero_chutado == numero_secreto):
    print("Você acertou!!")
else:
    print("Você errou!!")
