'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

n = int(input('Digite um número: '))

d = n*2
t = n*3
rq = n** (1/2)

print('O dobro de {} é {}, o triplo é {} \ne a raiz quadrada é {:.2f}'.format(n, d , t, pow(n, (1/2))))