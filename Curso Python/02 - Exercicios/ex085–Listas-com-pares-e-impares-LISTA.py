"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.
"""

numeros = [[],[]]

for c in range(1, 8):
    numero = int(input(f'Digite o {c}º valor: '))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print('-=' * 30)
numeros[0].sort()
print(f'O valores pares digitados foram: {numeros[0]}')

numeros[1].sort()
print(f'Os valores ìmpares digitados foram: {numeros[1]}')
