idade = 0
idade_Maior25 = 0
idade_Menor25 = 0
soma = 0
total = 0

while idade != -1:
    idade = int(input('Digite sua idade ou -1 para encerrar: '))
    
    if idade != -1:
        if idade >= 25:
            idade_Maior25 += 1
        elif 0 < idade <= 25:
            idade_Menor25 += 1
        else:
            print('Idade inválida')

        soma = soma + idade
        total += 1
        media = soma / total

print('\nTotal de idades: {} \nMédia das idades: {} \nMaiores que 25: {} \nMenores que 25: {}'.format(total, media, idade_Maior25, idade_Menor25))