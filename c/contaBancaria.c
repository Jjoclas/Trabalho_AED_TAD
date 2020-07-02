#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <iostream>
#include "Contabancaria.h"
using namespace std;
void Inicializa(ContaBancaria* conta, int cpf, double saldo)
{
    (*conta).cpf = cpf;
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
    printf("CPF: %d\n", conta.cpf);
    printf("Saldo: %.2f\n", conta.saldo);
}
void Transferir (ContaBancaria* envia, double valor, ContaBancaria* recebe)
{
    if (Saque(envia,valor))
    {
        Deposito(recebe, valor);
    }
}

void initlista(lista *pRecebido)
{
    (pRecebido)->proximo = NULL;
}
void insertlista(lista *pRecebido)
{
//Declaracoes
    lista *temporario;
    ContaBancaria valor;
//Instrucoes
    cout<<"\n\tInforme um valor a ser inserido : ";
    cin>>valor;
    temporario = (lista * )malloc(sizeof(lista));
    temporario->conta = valor;
    temporario->proximo = (pRecebido)->proximo;
    (pRecebido)->proximo = temporario;
}
void buscalistasimples(lista *pRecebido)
{
    //Declaracoes
    lista *temporario;
    int i=0;
    //Instrucoes
    if((pRecebido)->proximo == NULL)
    {
        cout<<"\tLista Vazia!\n";
    }else
    {
        temporario = (lista * )malloc(sizeof(lista));
        temporario = (pRecebido)->proximo;
        system("cls");
        while(temporario!=NULL)
        {
            cout<<"\n\t["<<(i=i+1) <<"] Valor : "<<temporario->conta<<"\n";
            temporario = temporario->proximo;
        }
    }
}