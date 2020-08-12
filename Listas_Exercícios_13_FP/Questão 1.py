num_clientes = int(input('Quantos clientes há na loja? '))

bonus_total = 0
clientes_aptos = 0

for cliente in range(num_clientes):
    cliente_nome = input('\nDigite seu nome: ')
    valor_gasto = float(input('Digite o valor gasto: '))

    if valor_gasto >= 2000:
        bonus = valor_gasto * 0.15
        bonus_total = bonus_total + bonus
        clientes_aptos += 1

        print('O cliente {} está apto para receber o bônus.'.format(cliente_nome))
print('Clientes:', clientes_aptos)
print('Total: R${}'.format(bonus_total))


