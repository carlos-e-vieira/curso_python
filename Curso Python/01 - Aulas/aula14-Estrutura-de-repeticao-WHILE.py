'''
# meu teste
nome = ''
senha = ''
limite = 0

while nome != 'Cal' and senha != 123:
    nome = str(input('Nome: '))
    senha = int(input('Senha: '))
    limite += 1
    if limite == 3:
        print('LIMITE excedido! Tente novamente mais tarde!')
        exit()

print('Acesso liberado!')
'''

'''
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
'''

'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')
'''

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Quantidade de números pares: {}'.format(par))
print('Quantidade de números impares: {}'.format(impar))
print('Acabou')