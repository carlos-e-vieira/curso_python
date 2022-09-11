'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

# minha solução
flag = soma = contador = 0
while flag != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        flag = 999
    else:
        soma = soma + n
        contador += 1
print('Você digitou {} números e a soma deles foi {}'.format(contador, soma))
