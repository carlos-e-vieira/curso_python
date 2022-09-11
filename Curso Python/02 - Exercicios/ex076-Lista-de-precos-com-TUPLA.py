"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, 
mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('Lápis', 1.75,
            'Borracha', 2.50,
            'Caderno', 4.75,
            'Mochila', 120.00,
            'Lapizeira', 12.00,
            'Livro', 32.00)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end=' ')
    else:
        print((f'R${listagem[posicao]:>7.2f}'))

print('-'*40)
