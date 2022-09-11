'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

# minha tentativa
print('-'*40)
print('LOJA SUPER BARATINHA')
print('-'*40)

total = totmil = menor = contador = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    contador += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if contador == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'NS':
        resp = str(input(('Quer continuar? [S/N]'))).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
