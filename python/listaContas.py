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
        retorno = True
        for conta in self.lista:
            if conta.agencia == numeros[0] and conta.numero == numeros[1]:
                retorno = False
                return conta
        if retorno:
            print('Agencia ou numero da conta invalidos')
            print('Tente inserir a conta novamente')
            self.indentificaConta(input('Formato (XXXX 12345). Agencia (espaço) numero da conta.\n'))
    
    @staticmethod
    def agencias():
        agencias = {
            'Sao Paulo' : 1243,
            'Rio de Janeiro' : 3421,
            'Belo Horizonte' : 1001,
            'Salvador' : 2134
        }
        return agencias

