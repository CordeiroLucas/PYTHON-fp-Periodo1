estado = input('Digite um caracter para representar seu estado civil: ')

lista = ['Casado', 'Divorciado', 'Solteiro', 'Viuvo']
if estado == 'c':
    print(lista[0])
elif estado == 'd':
    print(lista[1])
elif estado == 's':
    print(lista[2])
elif estado == 'v':
    print(lista[3])
else:
    print('Erro, caracter inválido')