1) Desenvolva um CRUD* de Alunos onde as seguintes informações devem ser
manipuladas:

Alunos

- CPF (Identificador - será usado como chave para consulta, edição e remoção)
- Nome
- Nota 1
- Nota 2
- Média (calculada pelo sistema, usando as notas 1 e 2)

- Situação (calculada pelo sistema, usando a média:
● A → media >= 7
● F → media >= 4 e media < 7
● R → media < 4

As opções apresentadas ao usuário serão:

Opções

Controle de Alunos

1 - Listar Alunos
2 - Cadastrar Alunos
3 - Consultar Aluno (chave: CPF)
4 - Editar Aluno (chave: CPF)
5 - Remover Aluno (chave: CPF)
6 - Listar Nomes dos Alunos Aprovados
7 - Listar Quantidade de Alunos por Situação
8 - Mostrar Média de Notas da Turma
9 - Apresentar o Nome e Nota do Aluno com Maior Nota
10 - Apresentar o Nome e Nota do Aluno com Menor Nota
-1 - Encerrar programa
