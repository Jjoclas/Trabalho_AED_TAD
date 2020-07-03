import re
import sys
from contaBancaria import ContaBancaria




def menu (lista):
    print('APK Investimentos')
    
    print('1- Criar Conta')
    print('2- Realizar Deposito')
    print('3- Realizar Saque')
    print('4- Transferencia entre contas')
    print('5- Consultar conta')
    print('0- Sair')

    escolha = int(input('Escolha uma das opções para continuar \n'))
    if escolha == 1:
        criarConta(lista)
        voltar(lista)
    elif escolha==2:
        realizarDeposito(lista)
        voltar(lista)
    elif escolha==3:
        realizarSaque(lista)
        voltar(lista)
    elif escolha==4:
        realizarTransferencia(lista)
        voltar(lista)
    elif escolha==5:
        realizaConsulta(lista)
        voltar(lista)
    elif escolha==0:
        finaliza()
    else:
        print('escolha uma opção valida')
        menu(lista)
def finaliza():
    print('Finalizando programa')
    sys.exit()   

def voltar(lista):
    escolha = int(input('Para voltar ao menu digite 1. Para sair digite outro \n'))
    if escolha == 1:
        menu(lista)
    else:
        finaliza()

def criarConta(lista):
    agencia = defAgencia()
    cpf = defCpf()
    nome = input('Informe seu nome. \n')
    saldo = validaValor()
    
    conta = ContaBancaria(agencia,cpf,nome,saldo)
    lista.adicionaConta(conta)

    print('Os dados da sua conta são:')
    conta.imprime()

def realizarDeposito(lista):
    valor = validaValor()
    conta = lista.indentificaConta(input('Informe a agencia e o numero da conta no formato (XXXX 12345). Separados por espaço\n'))
    conta.deposito(valor)
   
def realizarSaque(lista):
    valor = validaValor()
    conta = lista.indentificaConta(input('Informe a agencia e o numero da conta no formato (XXXX 12345). Separados por espaço\n'))
    conta.saque(valor)

def realizarTransferencia(lista):
    envia = lista.indentificaConta(input('De qual conta será transferido?\n Formato (XXXX 12345). Separados por espaço\n'))
    valor = validaValor()
    recebe = lista.indentificaConta(input('Para qual conta será transferido? \n Formato (XXXX 12345). Separados por espaço\n'))
    if envia.saque(valor):
        recebe.deposito(valor)
        print('transferencia concluida com sucesso')

def realizaConsulta(lista):
    conta = lista.indentificaConta(input('Informe a agencia e o numero da conta no formato (XXXX 12345). Separados por espaço\n'))
    conta.imprime()

def validaValor():
    saldo = int(input('Informe o valor. \n'))
    if saldo>0:
        return saldo
    else:
        print('Valor invalido, por favor preencha novamente')
        validaValor()
def agencias():
    agencias = {
        'Sao Paulo' : 1243,
        'Rio de Janeiro' : 3421,
        'Belo Horizonte' : 1001,
        'Salvador' : 2134
    }
    return agencias
def defAgencia():
    mostraAgencias()
    agencia =input('Escolha a cidade que melhor te atenda. \n')
    retorno = True
    print(agencia)
    for cidades, numero in agencias().items():
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
    for keys in agencias().keys():
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
 
