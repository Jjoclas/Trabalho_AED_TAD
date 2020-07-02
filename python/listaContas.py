import numpy as np

class Lista:
    def __init__(self):
        self.lista = []

    def Transferir(self, envia, valor, recebe):
        envia = self.indentificaConta(envia)
        recebe = self.indentificaConta(recebe)
        if(envia.saque(valor)):
            recebe.deposito(valor)
        else:
            print("Saldo insuficiente para transferencia. Seu saldo atual é de " + envia.saldo)
    def adicionaConta(self, conta):
        self.lista.append(conta)
    
    def imprimeConta(self,numero):
       conta = self.indentificaConta(numero)
       conta.imprime()
    def indentificaConta(self,numero):
        numero = numero.split(" ")
        numeros = [int(int(val)) for val in numero]
        
        for conta in self.lista:
            if conta.numero == numero:
                return conta
    @staticmethod
    def agencias():
        agencias = {
            'Sao Paulo' : 1243,
            'Rio de Janeiro' : 3421,
            'Belo Horizonte' : 1001,
            'Salvador' : 2134
        }
        return agencias

