# Por Liubliana Stolz e Lucas Pacheco
# cpf// nome// nota 1// nota 2// media// situacao (a, f, r)

cpf = [1, 2, 3, 4, 5]
situacoes = ['A', 'A', 'F', 'R', 'R']
nomes = ['Marenho', 'Mathiu', 'Liu', 'Luxca', 'Gold']
nota1 = [10, 8, 6, 3, 4]
nota2 = [9, 8, 7, 4, 3]
media = [9.5, 8, 6.5, 3.5, 3.5]
aprovados = ['Marenho', 'Mathiu']
opcao = 0
sn = 'sim'

while opcao != -1:
    x = 'CRUD DE ALUNOS'
    print('\n{:*^100}'.format(x))
    print('\n\n1 - Listar alunos')
    print('2 - Cadastrar alunos')
    print('3 - Consultar aluno')
    print('4 - Editar aluno')
    print('5 - Remover aluno')
    print('6 - Listar nomes dos alunos aprovados')
    print('7 - Listar quantidade de alunos por situação')
    print('8 - Mostrar média de notas da turma')
    print('9 - Apresentar o nome e nota do aluno com maior nota ')
    print('10 - Apresentar nome e nota do aluno com menor nota ')
    print('-1 - Finalizar\n')

    opcao = int(input('Digite uma das opções acima:\n'))

    if opcao != -1:
        if opcao == 1:
            print('Nomes:', nomes)
            op = input('Pressione enter para voltar\n')


        elif opcao == 2:
            nome = input('Digite seu nome: ')
            nomes.append(nome)
            nota1.append(float(input('Digite a nota 1: ')))
            nota2.append(float(input('Digite a nota 2: ')))
            cpf.append(int(input('Digite o seu cpf: ')))
            media_num = (nota1[-1] + nota2[-1]) / 2
            media.append(media_num)

            if media_num >= 7:
                situacao = 'A'
                situacoes.append(situacao)
                aprovados.append(nome)
            elif 4 <= media_num < 7:
                situacao = 'F'
                situacoes.append(situacao)
            elif media_num < 4:
                situacao = 'R'
                situacoes.append(situacao)

        elif opcao == 3:
            cpf_consulta = int(input("\nDigite o CPF: "))
            posicao = cpf.index(cpf_consulta)

            print('Nome: ', nomes[posicao])
            print('Nota 1: ', nota1[posicao])
            print('Nota 2:', nota2[posicao])
            print('CPF:', cpf[posicao])
            print('Média:', media[posicao])
            print('Situação: ', situacoes[posicao])
            op = input('Pressione enter para voltar\n')

        elif opcao == 4:
            cpf_consulta = int(input('Digite o CPF: '))

            while sn == 'sim':
                posicao = cpf.index(cpf_consulta)
                print('1 - Alterar nome')
                print('2 - Alterar nota1')
                print('3 - Alterar nota2')
                opcaoE = int(input('\nDigite o que você deseja fazer com o aluno {}: \n'.format(nomes[posicao])))
                if opcaoE == 1:
                    print('Nome antigo: ', nomes[posicao])
                    nome = input('Digite o novo nome: ')
                    nomes.pop(posicao)
                    nomes.insert(posicao, nome)

                elif opcaoE == 2:
                    print('Nota antiga: ', nota1[posicao])
                    nota1.pop(posicao)
                    nota = float(input('Digite a nota 1: '))
                    nota1.insert(posicao, nota)
                    media_num = (nota1(posicao) + nota2(posicao)) / 2

# Caso mudem a media, para fazer mudar a situacao
# tirar ou colocar na lista de aprovado ta bugando MUITO

                    if media_num >= 7:
                        situacao = 'A'
                        situacoes.pop(posicao)
                        situacoes.insert(posicao, situacao)
                        if nome not in aprovados:
                            aprovados.insert(posicao, nome)

#Caso mudem a media, para fazer mudar a situacao
#tirar ou colocar na lista de aprovado ta bugando MUITO

                    elif 4 <= media_num < 7:
                        situacao = 'F'
                        situacoes.pop(posicao)
                        situacoes.insert(posicao, situacao)
                        if nome in aprovados:
                            aprovados.pop(posicao)

                    elif media_num < 4:
                        situacao = 'R'
                        situacoes.pop(posicao)
                        situacoes.insert(posicao, situacao)
                        if nome in aprovados:
                            aprovados.pop(posicao)

                elif opcaoE == 3:
                    print('Nota antiga: ', nota2[posicao])
                    nota2.pop(posicao)
                    nota = float(input('Digite a nota 2: '))
                    nota2.insert(posicao, nota)
                    media_num = (nota1(posicao) + nota2(posicao)) / 2
                else:
                    print('Opção inválida')

                sn = input('\nVocê deseja editar mais alguma coisa?\n(Digite sim ou nao)  ')
                if sn == 'nao':
                    break

        elif opcao == 5:
            cpf_consulta = int(input('\nDigite o cpf: '))
            posicao = cpf.index(cpf_consulta)
            nome = nomes[posicao]
            if nome in aprovados:
                posicao2 = aprovados.index(nome)
                aprovados.pop(posicao2)
            nomes.pop(posicao)
            nota1.pop(posicao)
            nota2.pop(posicao)
            cpf.pop(posicao)
            media.pop(posicao)

        elif opcao == 6:
            i = 0
            maximo = len(aprovados)

            while i < maximo:
                print(aprovados[i])
                i = i + 1

            op = input('Pressione enter para voltar\n')

        elif opcao == 7:
            print('Quantidade de aprovados:', situacoes.count('A'))
            print('Quantidade de finalistas:', situacoes.count('F'))
            print('Quantidade de reprovados:', situacoes.count('R'))
            op = input('Pressione enter para voltar')

        elif opcao == 8:
            media
            print('Meida de notas da turma ', sum(media) / len(media))
            op = input('Pressione enter para voltar')

        elif opcao == 9:
            maior = max(media)
            posicao = media.index(maior)
            print('Nome:', nomes[posicao])
            print('Maior media:', maior)
            op = input('Pressione enter para voltar')

        elif opcao == 10:
            menor = min(media)
            posicao = media.index(menor)
            print('Nome:', nomes[posicao])
            print('Menor media:', menor)
            op = input('Pressione enter para voltar')

        else:
            print('Opção inválida')

print('\nVocê finalizou')
kbo = 'AMÉM QUE FINALIZOU'
print('{:*^100}'.format(kbo))