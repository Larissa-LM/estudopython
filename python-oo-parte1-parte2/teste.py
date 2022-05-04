def cria_conta(numero,titular,saldo,limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

def deposita(conta, valor): 
    conta ["saldo"] += valor

def saca(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

conta = cria_conta(123,"Larissa", 55.0, 1000.0) 
print(conta)

#Código que mostra a importância de oo, já que assim podemos criar contas sem todas as chaves ex: conta_l = {"numero": 404, "saldo": 50.0} conseguiria utilizar a fun depositar sem um titular e limite
# conseguiria também depositar sem chamar a func despositar ex: conta_l["saldo"] = conta_l["saldo"] + 300.0
# além disso se passarmos uma chave que não existe dentro do dicionário da função, quebra, ex: conta_x = {"numero": 097, "limite": 1000.0}, se jogarmos esse exemplo na func deposita, saca ou extrato
# quebra o código