dicionario = {}
s = 0
i = 0
for i in range(4):
    nome = input('Nome: ')
    seguidores = []

    for s in range(3):
        seguidor = int(input())
        seguidores.append(seguidor)

    dicionario[nome] = seguidores

medias = []

for nome in dicionario:
    seguidores = dicionario[nome]
    media = sum(seguidores)/len(seguidores)
    medias.append(media)
    dicionario[nome][1] = media
    print('{}: {:.2f}'.format(nome, media))

media_maior = max(medias)
media_menor = min(medias)
nome_maior = ''
nome_menor = ''

for nome in dicionario:
    if media_maior in dicionario[nome]:
        nome_maior = nome
    elif media_menor in dicionario[nome]:
        nome_menor = nome

print('\n{} teve a maior média de curtidas'.format(nome_maior))
print('{} teve a menor média de curtidas'.format(nome_menor))