bonus_total = 0
filho7menos = 0
filho8a17 = 0
for func in range(4):
    filhos = int(input('Número de filhos:'))
    i = 1
    if filhos > 0:
        while i <= filhos:
            filho_idade = int(input())
            if filho_idade <= 7:
                bonus_total = bonus_total + 250
                filho7menos += 1

            elif 7 < filho_idade <= 17:
                bonus_total = bonus_total + 150
                filho8a17 += 1
            i += 1
print('Até 7 anos:', filho7menos)
print('Entre 8 a 17 anos:', filho8a17)
print('Total de bônus:', bonus_total)

