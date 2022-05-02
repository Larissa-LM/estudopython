
class Conta: 
    
    def __init__(self,numero,titular,saldo,limite): #self é a referência que sabe encontrar o objeto construído em memória. 
        #utilizaremos self para acessar o objeto e definir seus atributos e características.
        self.numero = numero 
        self.titular = titular 
        self.saldo = saldo 
        self.limite = limite 
    
    def extrato(self): 
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
    
    def deposita(self, valor): 
        self.saldo += valor 

    def saca(self, valor): 
        self.saldo -= valor 