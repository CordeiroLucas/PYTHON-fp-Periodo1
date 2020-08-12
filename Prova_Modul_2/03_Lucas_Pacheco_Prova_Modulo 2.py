nomes50 = []
pesos50 = []
i = 0
while i < 5:
    peso = float(input('Peso: '))
    nome = input('\nNome: ')

    if peso >= 50:
        nomes50.append(nome)
        pesos50.append(peso)
        i += 1
tupla = (nomes50, pesos50)

print(tupla)