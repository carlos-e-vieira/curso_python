"""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são
variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis
por chaves individuais.
"""

lista1 = ['Nome:', 'Carlos']
lista2 = ['Eduardo', 'Vieira']
lista3 = [lista1, lista2]
print(lista3)
print('\n', end='')

# colocar lista(s) dentro de outra(s) lista(s) - Cópia
dados1 = ['Carlos', 39]
dados2 = ['Maria', 14]
dados3 = ['Eliana', 50]
pessoas1 = []
pessoas1.append(dados1[:])
pessoas1.append(dados2[:])
pessoas1.append(dados3[:])
print(pessoas1)
print('\n', end='')

pessoas2 = [['Carl', 25], ['Danda', 2], ['Li', 36]]
print(pessoas2)
print(pessoas2[2][0])
print(pessoas2[0][1])
print(pessoas2[1])
print('\n', end='')

# usando o for para percorrer um lista de listas
galera1 = [['Fabio', 31], ['Ivone', 55], ['Samanta', 19], ['Suelem', 14]]
posicao1 = 0
for idade in galera1:  # só a idade
    print(f'A idade do cadastro de posição {posicao1} é {idade[1]}')
    posicao1 += 1

for nome in galera1: # só os nomes
    print(f'Nome: {nome[0]}')

for pessoa in galera1:  # ver todos os dados
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
print('\n', end='')

#pegando dados no input
galera2 = []
dados4 = []
for c in range(0, 3):
    dados4.append(str(input('Nome: ')))
    dados4.append(int(input('Idade: ')))
    galera2.append(dados4[:])  # cópia de dados
    dados4.clear()  # limpa dados para receber novos dados enquanto o for existir
print(galera2)
# mostrar pessoas com mais de 21 anos
totalmaior = totalmenor = 0
for pessoa3 in galera2:
    if pessoa3[1] >= 21:
        print(f'{pessoa3[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{pessoa3[0]} é menor de idade')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')




