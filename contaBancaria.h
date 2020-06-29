
// definição do tipo
typedef struct {
 int numero;
 double saldo;
} ContaBancaria;
// cabeçalho das funções
void Inicializa(ContaBancaria* conta, int numero, double saldo);
void Deposito (ContaBancaria* conta, double valor);
int Saque (ContaBancaria* conta, double valor);
void Imprime (ContaBancaria conta);