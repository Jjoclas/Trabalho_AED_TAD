#include <stdio.h>
#include <stdlib.h>
#include "ContaBancaria.c"

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