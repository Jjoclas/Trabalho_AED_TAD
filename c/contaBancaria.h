#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <iostream>
// definição do tipo
typedef struct {
 int cpf;
 double saldo;
} ContaBancaria;
// cabeçalho das funções
void Inicializa(ContaBancaria* conta, int cpf, double saldo);
void Deposito (ContaBancaria* conta, double valor);
int Saque (ContaBancaria* conta, double valor);
void Imprime (ContaBancaria conta);

typedef struct lista{
    ContaBancaria conta;
    struct lista *proximo;
}lista;

void insertlista(lista *pRecebido);
void initlista(lista *pRecebido);
void buscalista(lista *pRecebido);


/*
   ContaBancaria conta1;
    Inicializa(&conta1, 1, 300.00);
    ContaBancaria conta2;
    Inicializa(&conta2, 2, 300.00);
    
    printf("\nAntes da movimentacao:\n ");
    Imprime(conta1);
    Deposito(&conta1, 50.00);
    Saque(&co Cnta1, 70.00);
    printf("\nDepois da movimentacao:\n ");
    Imprime (conta1);

    Transferir(&conta1,100.00,&conta2);
    printf("\nDepois da transferencia:\n ");
    Imprime (conta1);
    Imprime (conta2);
*/