idade = 1
idades = []
while idade > 0:
    idade = int(input('Digite a idade: '))
    if idade > 0:
        idades.append(idade)
    else:
        media = sum(idades)/len(idades)
        print('Quantidade de idades válidas: ', len(idades))
        print('A soma das idades: ', sum(idades))
        print('A média das idades: ', media)
        n = 0
        for valor in idades:
            if valor > media:
                n += 1
        print('Quant. de idades acima da media: ', n)
        n = 0
        for valor in idades:
            if valor < 25:
                n += 1
        print('Quant. de idades menores que 25: ', n)

print('Programa encerrado')