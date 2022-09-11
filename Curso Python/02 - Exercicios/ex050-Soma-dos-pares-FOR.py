'''
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for
ímpar, desconsidere-o.
'''

soma = 0
contador = 0

for cont in range(1, 7):
    num = int(input('Digite no {}º número: '.format(cont)))
    if num % 2 == 0:
        soma += num
        contador += 1

print('Você informou {} números PARES e a soma foi {}'.format(contador, soma))
