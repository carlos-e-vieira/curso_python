'''
for c in range(0, 3):
    print('Oi')
'''

'''
# decremento
for c2 in range(6, 0, -1):
    print(c2)
'''


'''
# incremento de 2
for c2 in range(0, 20, 2):
    print(c2)
'''

'''
n = int(input('Digite um número: '))
for c3 in range(0, n+1):
    print(c3)
print('FIM')
'''

'''
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
'''

s = 0

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))