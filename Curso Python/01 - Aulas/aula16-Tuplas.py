'''
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários
valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche[1]) # imprimi o elemento selecionado da tupla
print(lanche[-1]) # ultimo elemento
print(lanche[-2]) # penultimo elemento
print(lanche[1:3]) # do elemento 1 até chegar no 3
print(lanche[2:]) # do elemento especificado até o final
print(lanche[:-2]) # do inicio até o penutimo
print(lanche[:2]) # do inicio até chegar no elemento 2
print(lanche[-2:]) # começa no penultimo e vai até o final

# usando o for simples sem posição
print('='*30)
for comida in lanche:
    print(f'Eu comi {comida}!')
print('Nossa comi demais!')
print('='*30)

# usando o for com contador de indice
for contador in range(0, len(lanche)):
    print(f'Vou comer {lanche[contador]} da posição {contador}')
print('Vou comer demais!!!')
print('='*30)

# for precisando da posição com enumerate
for posicao, comida2 in enumerate(lanche):
    print(f'Eu vou comer {comida2} na posição {posicao}')

# Ordem Alfabética
print(sorted(lanche))

# teste de soma de valores
a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = b + a
soma = a[0] + b[-1]
print(soma) # somando valores
print(len(c)) # mostra o tamanho da tuple
print(c.count(5)) # mostra quantas vezes está aparecendo o número 5
print('-'*30)
print(c)
print(c.index(4)) # mostra em que posição está o elemento especificado
print(c.index(5, 1)) # mostra o primeiro 5 apartir da posição 1
print('-'*30)

# varios tipos de dados em uma tupla
pessoa = ('Carlos', 39, 'M', 85.55)
# del(pessoa) # del() apaga os valor da tupla
print(f'Meu nome é {pessoa[0]}, tenho {pessoa[1]} anos, sou do sexo {pessoa[2]} e tenho {pessoa[3]} kilos.')
