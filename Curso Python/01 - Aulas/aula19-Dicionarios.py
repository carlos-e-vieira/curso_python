"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma
mesma estrutura, acessíveis por chaves literais.
"""

filmes1 = {'titulo': 'Matrix', 'ano': 2001, 'Diretor': 'Irmãs Walsjaski'}
print(filmes1.values())  # retorna todos os valores do dicionário
print(filmes1.keys())  # retorna o nome dos indices do dicionário
print(filmes1.items())  # retona values e keys
# imprimir usando for
for k, v in filmes1.items():
    print(f'O {k} é {v}')
print('=-' * 30, '\n', end='')


# LISTAS COM DICIONARIOS
filmes_2 = {'titulo': 'Matrix', 'ano': 2001, 'diretor': 'Irmãs Walsjaski'}
filmes_3 = {'titulo': 'Clube da Luta', 'ano': 1999, 'diretor': 'Kevin Space'}
filmes_4 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}

locadora = (filmes_2, filmes_3, filmes_4)
print(locadora[0]['ano'])
print(locadora[2]['diretor'])
print('=-' * 30, '\n', end='')


# SEGUNDO A AULA
pessoas_1 = {'nome': 'Carlos', 'idade': 39, 'sexo': 'M'}
print(pessoas_1)
print(f"O {pessoas_1['nome']} tem {pessoas_1['idade']} anos")
print(pessoas_1.values())  # retorna todos os valores do dicionário
print(pessoas_1.keys())  # retorna o nome dos indices do dicionário
print(pessoas_1.items())  # retona values e keys

# acessar os valores por lações
for chaves in pessoas_1.keys():
    print(chaves)

for valores in pessoas_1.values():
    print(valores)

for chaves, valores in pessoas_1.items():
    print(f'{chaves}: {valores}')
print('=-' * 30, '\n', end='')


# APAGANDO ELEMENTOS -> KEYS
pessoas_2 = {'nome': 'Carlos', 'idade': 39, 'sexo': 'M'}
del pessoas_2['sexo']
print(pessoas_2.items())
print('=-' * 30, '\n', end='')


# ALTERANDO VALORES
pessoas_3 = {'nome': 'Carlos', 'idade': 39, 'sexo': 'M'}
pessoas_3['nome'] = 'Dandara'
print(pessoas_3.items())
print('=-' * 30, '\n', end='')

# ADICINAR KEYS
pessoas_4 = {'nome': 'Carlos', 'idade': 39, 'sexo': 'M'}
pessoas_4['peso'] = 85.5
print(pessoas_4.items())
print('=-' * 30, '\n')


# DICIONARIO DENTRO DE UMA LISTA
brasil_1 = []
estado_1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado_2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil_1.append(estado_1)
brasil_1.append(estado_2)

print(brasil_1)
print(brasil_1[0])
print(brasil_1[1])
print(brasil_1[0]['uf'])
print('=-' * 30, '\n')


# FAZENDO COPIAS DE DICIONARIO EM UMA LISTA
estado_3 = dict()
brasil_3 =  list()
for c in range(0, 3):
    estado_3['uf'] = str(input('Unidade Federativa: '))
    estado_3['sigla'] = str(input('Sigla do Estado: '))
    brasil_3.append(estado_3.copy())
print(brasil_3)

for estado in brasil_3:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')