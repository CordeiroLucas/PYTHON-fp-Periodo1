cidades = []
i = 0
while i < 5:
    cidade_e_temp = []
    cidade = input('Cidade: ')
    cidade_e_temp.append(cidade)
    temperatura = float(input('Temperatura: '))
    cidade_e_temp.append(temperatura)
    cidades.append(cidade_e_temp)
    i += 1
print('') #Só para dar um único espaçamento mesmo
for lista in cidades:
    f = lista[1] * 1.8 + 32
    print('{} {}°F'.format(lista[0], f))