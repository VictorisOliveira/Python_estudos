class conta:
    def __init__(self, nome,numero):
        self.Cliente = nome
        self.num = numero
        self.saldo = 0.0

    def saldo(self):
        return self.saldo
    
    def getCliente(self):
        return self.Cliente
    
    def Depositar(self, valor):
        self.saldo += valor         
    
     