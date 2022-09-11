'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.
'''

temp = float(input('Informe a temperatura em ºC: '))

conversao = ((9 * temp) / 5) + 32

print('A temperatuda de {:.1f}ºC correspende a {:.1f}ºF!'.format(temp, conversao))