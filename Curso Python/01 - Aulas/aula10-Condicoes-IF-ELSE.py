'''nome = str(input('Digite seu nome: '))
if nome == 'Carlos':
    print('Seu nome é lindo!')
else:
    print('Seu nome é bem normal :(')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média da sua nota é {:.1f}'.format(m))
#print('PARANÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')

if m >= 6.0:
    print('Sua média está ótima!')
else:
    print('Sua média está ruim :(')