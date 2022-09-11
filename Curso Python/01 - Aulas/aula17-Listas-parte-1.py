"""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
"""

lista1 = ['casa', 'jardim', 'carro']
print(lista1)
lista1[0] = 'apartamento'
print(lista1)
print('\n', end='')

# append('') adiciona novo elemento no final da lista
lista1.append('moto')
print(lista1)
print('\n', end='')

# insert(0, '') adiciona um elemento na posição especificada
lista2 = ['gato', 'cachorro', 'periquito']
lista2.insert(0, 'pet')
print(lista2)
print('\n', end='')

# remover um elemento pelo indice especificado
lista3 = ['cama', 'gaiola', 'gaveta', 'estante']
print(lista3)
del lista3[0]
print(lista3)

lista4 = ['pneu', 'banco', 'motor', 'vidro']
print(lista4)
lista4.pop(0)
print(lista4)
print('\n', end='')

# remover um elemento pelo valor
lista5 = ['médico', 'enfermeira', 'sonda']
print(lista5)
lista5.remove('sonda')
print(lista5)
print('\n', end='')

# remove o ultimo elemento da lista
lista6 = ['amor', 'carinho', 'paixão']
print(lista6)
lista6.pop()
print(lista6)
print('\n', end='')

# verificar se existe um elemento para ser excluido
lista7 = ['mármore', 'argila', 'barro', 'areia']
print(lista7)
if 'areia' in lista7:
    lista7.remove('areia')
    print(lista7)
print('\n', end='')

# criar listas através de ranges passados com paramentro
# cria uma estrutura ordenada de forma crescente
valores1 = list(range(5, 12, 2))
# valores1 = list(range(5, 12, 3)) # pulando de 3 em 3
print(valores1)
print('\n', end='')

# criar uma lista sem ordem e colocar em ordem
valores2 = [9, 2, 5, 4, 7, 3, 1, 8]
print(valores2)
valores2.sort()
print(valores2)
print('\n', end='')

# criar a ordem inversa
valores3 = [5, 9, 7, 3, 6, 1]
print(valores3)
valores3.sort(reverse=True)
print(valores3)
print('\n', end='')

# ver quantos elementos tem em uma lista
valores4 = [1, 4, 7, 2, 5, 8, 9, 6, 3]
print(valores4)
print(f'A lista valores4 tem {len(valores4)} elementos')
print('\n', end='')

# adicionando valores com append
valores5 = []
valores5.append(5)
valores5.append(9)
valores5.append(2)

for indice, valor in enumerate(valores5): # enumetera pega o indice e o valor
    print(f'O valor {valor} foi adicinado na posição {indice}!')
print('Acabou a lista!')

# adicionando valor através do input
"""valores6 = []
for cont in range(0, 4):
    valores6.append(int(input('Digite um valor: ')))

for indice, valor in enumerate(valores6):
    print(f'Adicionado o valor {valor} na posição {indice}º')
print(valores6)"""
print('\n', end='')

# fazer uma ligação entre listas
a = [1, 6, 9, 8]
b = a
b[0] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('\n', end='')

# fazer uma cópia de listas
a1 = [2, 5, 8, 9, 6]
b1 = a1[:]
b1[0] = 1
print(f'Lista A1: {a1}')
print(f'Lista B1: {b1}')
