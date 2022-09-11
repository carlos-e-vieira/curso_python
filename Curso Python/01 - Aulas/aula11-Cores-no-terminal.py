'''print('\033[0;30;41m Teste \033[m \n')
print('\033[4;33;44m Teste \033[m \n')
print('\033[1;35;43m Teste \033[m \n')
print('\033[30;42m Teste \033[m \n')
print('\033[m Teste \033[m \n')
print('\033[7;30m Teste \033[m \n')'''

print('\033[7;30mOlá mundo\033[m')

a = 5
b = 7
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Carlos'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[35m', nome, '\033[m'))

cores = {'limpa':'\033[m','azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

print(3 * 5 + 4 ** 2)