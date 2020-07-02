#include <stdio.h>
#include <stdlib.h>
#include "ContaBancaria.c"

void menu()
{
    printf("Menu:\n ");
    printf("1: Criar uma &conta:\n ");
    printf("2: Realizar deposito:\n ");
    printf("3: Realizar Saque:\n ");
    printf("4: Transferencia entre contas:\n ");
    printf("5: Consultar saldo:\n ");
    printf("0: Sair:\n ");
    opcao();
}
/*
void opcao(){
    int opcao;
    ContaBancaria conta;
    int cpf;
    int valor;
    int recebe;
    scanf("%d", &opcao);
    system("cls || clear");

    switch(continuar)
    {
        case 1:
            Inicializa(&conta,cpf,valor);
            break;

        case 2:
            Deposito(&conta,valor);
            break;

        case 3:
            Saque(&conta,valor);
            break;

        case 4:
            transferir(&conta, valor, &recebe);
            break;
        
        case 5:
            Imprime(&conta);
            break;
        
        case 0:
            
            break;

        default:
            printf("Digite uma opcao valida\n");
    }
}
*/
int main (int argc, char **argv)
{
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
}