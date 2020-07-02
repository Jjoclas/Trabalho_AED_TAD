import re
from contaBancaria import ContaBancaria
from listaContas import Lista as lt



def menu ():
    print('Bem vindo ao banco APK Investimentos')
    
    print('1- Criar Conta')
    print('2- Realizar Deposito')
    print('3- Realizar Saque')
    print('4- Transferencia entre contas')
    print('0- Sair')

    escolha = int(input('Escolha uma das opções para continuar'))

def criarConta(lista):
    agencia = defAgencia()
    cpf = defCpf()
    nome = input('Informe seu nome. \n')
    saldo = validaValor()
    
    conta = ContaBancaria(agencia,cpf,nome,saldo)
    lista.adicionaConta(conta)

    print('Os dados da sua conta são:')
    conta.imprime()
def realizarDeposito():
    valor = validaValor()
    conta = ()


def validaValor():
    saldo = int(input('Informe o valor do seu deposito. \n'))
    if saldo>0:
        return saldo
    else:
        print('Valor invalido, por favor preencha novamente')
        validaValor()
def defAgencia():
    mostraAgencias()
    agencia =input('Escolha a cidade que melhor te atenda. \n')
    retorno = True
    print(agencia)
    for cidades, numero in lt.agencias().items():
        if cidades.lower() == agencia.lower():
            agencia = numero
            retorno = False
            break
    if (retorno):
        print('Cidade invalida, Por favor informe uma das cidades na lista. \n')
        defAgencia()
    return agencia

def mostraAgencias():
    n =1
    for keys in lt.agencias().keys():
        print(keys)
        n+=1

def defCpf():
    cpf = input('Informe seu CPF: \n')
    if isCpfValid(cpf):
        return cpf
    else:
        print('CPF invalido, por favor preencha novamente')
        defCpf()
def isCpfValid(cpf):
    """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cpf,str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cpf)
    
    # Verify if CPF number is equal
    if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
        return False

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False
 