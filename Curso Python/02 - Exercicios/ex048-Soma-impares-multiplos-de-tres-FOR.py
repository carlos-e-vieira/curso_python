'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de
três e que se encontram no intervalo de 1 até 500.
'''

soma = 0
contador = 0

for c in range(3, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))
