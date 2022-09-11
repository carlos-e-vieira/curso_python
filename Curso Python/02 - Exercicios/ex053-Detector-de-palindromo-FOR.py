'''
Crie um programa que leia uma frase qualquer e diga se ela
é um palíndromo, desconsiderando os espaços.
'''

# strip() tira os espaços e upper() deixa tudo em maiúsculo
frase = str(input('Digite uma frase? ')).strip().upper()

# split() separa a franse em palavras (lista)
palavras = frase.split()

# ''.join() junta tudo sem espaço
junto = ''.join(palavras)

# fatiamento que inverte a frase
inverso = junto[::-1]

'''inverso = ''
# len() numero de letras da string
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um a Palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')