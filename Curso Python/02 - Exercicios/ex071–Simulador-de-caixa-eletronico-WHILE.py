'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues. OBS:
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

print('=' * 30)
print('{:^30}'.format('BANCO KALL'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break