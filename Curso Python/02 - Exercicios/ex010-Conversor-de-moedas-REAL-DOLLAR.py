'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.
'''

real = float(input('Digite o quanto você tem em real: '))
dolar = 3.27

conversao = real / dolar

if real >= dolar:
    print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, conversao))
else:
    print('Você não tem dinheiro para comprar nem US$1.00 seu pobre')
