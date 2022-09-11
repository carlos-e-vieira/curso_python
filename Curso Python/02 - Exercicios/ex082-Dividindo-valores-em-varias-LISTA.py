"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

listaCompleta = []
listaPares = []
listaImpares = []

while True:
    n = int(input('Digite um valor: '))
    listaCompleta.append(n)

    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)

    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 30)
print(f'A lista completa é {listaCompleta}')
print(f'A lista de pares é {listaPares}')
print(f'A lista de ímpares é {listaImpares}')