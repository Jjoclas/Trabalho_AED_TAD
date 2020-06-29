#include <stdio.h>
#include <stdlib.h>
#include "ContaBancaria.h"
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
int main (int argc, char **argv)
{
    ContaBancaria conta1;
    Inicializa(&conta1, 1, 300.00);
    ContaBancaria conta2;
    Inicializa(&conta2, 2, 300.00);
    
    printf("\nAntes da movimentacao:\n ");
    Imprime(conta1);
    Deposito(&conta1, 50.00);
    Saque(&conta1, 70.00);
    printf("\nDepois da movimentacao:\n ");
    Imprime (conta1);

    Transferir(&conta1,100.00,&conta2);
    printf("\nDepois da transferencia:\n ");
    Imprime (conta1);
    Imprime (conta2);
}