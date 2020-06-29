#include <stdio.h>
#include "Contabancaria.h"
void Inicializa(ContaBancaria* conta, int numero, double saldo)
{
    (*conta).numero = numero;
    (*conta).saldo = saldo;
}
void Deposito (ContaBancaria* conta, double valor)
{
    (*conta).saldo += valor;
}
int Saque (ContaBancaria* conta, double valor)
{
    double saldo;
    saldo = (*conta).saldo;
    if ((saldo - valor) <0)
    {
        printf("Saldo Insuficiente");
        return 0; 
    } else
    {
    (*conta).saldo -= valor;
        return 1; 
    }
}
void Imprime (ContaBancaria conta)
{
    printf("Numero: %d\n", conta.numero);
    printf("Saldo: %2f\n", conta.saldo);
}
void Transferir (ContaBancaria* envia, double valor, ContaBancaria* recebe)
{
    if (Saque(envia,valor))
    {
        Deposito(recebe, valor);
    }
}