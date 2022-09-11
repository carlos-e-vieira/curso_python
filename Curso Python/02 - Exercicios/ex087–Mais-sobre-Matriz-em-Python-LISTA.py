"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

soma_pares = soma_coluna_3 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)
for lin in range(0, 3):
    for col in range(0, 3):
        if matriz[lin][col] % 2 == 0:
            soma_pares += matriz[lin][col]
print(f'A soma dos valores pares é {soma_pares}')

for c in range(0, 3):
    soma_coluna_3 += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna_3}')

matriz[1].sort()
print(f'O maior valor da segunda coluna é {matriz[1][2]}')

