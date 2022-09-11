'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numExtenso = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
              'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número: '))

    if num >= 0 and num <= 20:
        print(f'Você digitou o número {numExtenso[num]}')

        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break

    print('Tente novamente. ', end='')
print('FIM DO PROGRAMA')
