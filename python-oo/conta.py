
class Conta: 
    
    def __init__(self,numero,titular,saldo,limite): #self é a referência que sabe encontrar o objeto construído em memória. 
        #utilizaremos self para acessar o objeto e definir seus atributos e características.
        self.__numero = numero 
        self.__titular = titular 
        self.__saldo = saldo 
        self.__limite = limite  # O __ antes do atributo torna ele privado
    
    def extrato(self): 
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposita(self, valor): 
        self.__saldo += valor 

    def saca(self, valor): 
        self.__saldo -= valor
    
    def transfere(self, valor, destino): 
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self): 
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite   
