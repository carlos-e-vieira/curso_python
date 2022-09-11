'''
 Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade
 e quantas já são maiores.
'''

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0

for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tiveram {} pessoas maiores de idade'.format(totalmaior))
print('E também tiveram {} pessoas menores de idade'.format(totalmenor))
