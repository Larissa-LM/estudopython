def cria_conta(numero,titular,saldo,limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

conta = cria_conta(123,"Larissa", 55.0, 1000.0) 
print(conta)
