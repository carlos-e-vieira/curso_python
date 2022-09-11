"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = []
maior = 0
menor = 0

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {v}: ')))
    maior = max(valores)
    menor = min(valores)

print('=-'*30)
print(f'Você digitou os valores {valores}')

#maior e indices que aparece
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}... ', end='')

# menor e indices que aparece
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}... ', end='')