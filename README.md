# desafio-dio-sistema-bancario

# Desafios do projeto:

### Implementar operações de:

- [x] Saque
- [x] Deposito
- [x] Extrato

### Regras:

- Depositos devem ser valores positivos
- Todos os depositos devem ser armazenados em uma variavel e exibidos na operaçao de extrato
- O sistema deve permitir apenas 3 saques diarios com limite de R$ 500 por saque
- Se não houver saldo: Deve emitir uma mensagem informando que não sera possivel sacar por falta de saldo
- Todos os saques devem ser armazenados em uma variavel e exibidos na operaçao de extrato
- O extrato deve listar todos os depositos e saques realizados
- Ao final da listagem deve ser exibido o saldo da conta
- Se o extrato estiver vazio exibir a mensagem: Não foram realizadas movimentações
- Os valores devem ser exibidos utilizando o formato R$ 000.00

# Segunda parte do projeto:

### Atualizações:

- Implementar funções para as operações existentes
- Implementar função de cadastrar usuario (cliente) e cadastrar conta bancaria
- A conta do banco (conta corrente) deve ser vinculada a um usuario
- Função saque: Recebe argumentos apenas por nome (keyword only). As mesmas regras anteriores devem ser aplicadas
- Função deposito: Recebe argumentos apenas por posição (positional only). As mesmas regras anteriores devem ser aplicadas
- Funçao extrato: Recebe argumentos por posição e nome (positional only e keyword only). As mesmas regras anteriores devem ser aplicadas
- Função criar usuario: Deve armazenar os usuarios em uma lista
- Um usuario é composto por: nome, data de nascimento, cpf e endereço
- Deve ser armazenado apenas o cpf
- Não deve ser possivel cadastrar dois usuarios com cpf iguais
- Função criar conta: Deve armazenar as contas em uma lista
- Uma conta é composta por: âgencia, numero da conta e usuario
- O numero da conta é sequencial iniciando em 1
- O numero da agencia é fixo: 0001
- O usuario pode ter mais de uma conta, mas uma conta pertence somente a um usuario
