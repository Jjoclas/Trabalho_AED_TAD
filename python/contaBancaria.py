import itertools 

class ContaBancaria:
    id_generator = itertools.count(10000)
    def __init__(self, agencia, cpf, nome, saldo):
        self.agencia = agencia
        self.numero = next(self.id_generator)
        self.cpf = cpf
        self.nome = nome
        self.saldo = saldo

    def saque(self, valor):
        if((self.saldo-valor)>0):
            self.saldo -=valor
            return True
        else:
            print("Saldo insuficiente. Seu saldo atual é de " + self.saldo)
            return False

    def deposito(self, valor):
        self.saldo +=valor
    
    def imprime(self):
        print('Numero da Agencia', self.agencia)
        print('Numero da conta: ', self.numero)
        print('CPF: ', self.cpf)
        print('Nome: ', self.nome)
        print('Saldo = ', self.saldo)
