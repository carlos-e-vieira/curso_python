"""
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
"""

def pula_trexos():
    print('-=' * 30, '\n')


# BASICO DA FUNÇÃO ----------------------------------------------------
def mostra_linha():
    print('-' * 40)

mostra_linha()
print(f'{"Carlos":^40}')
mostra_linha()
mostra_linha()
print(f'{"Li":^40}')
mostra_linha()
mostra_linha()
print(f'{"Dandara":^40}')
mostra_linha()
pula_trexos()


# FUNÇÃO COM PARAMETRO ----------------------------------------------------
def titulo_personalizado(titulo):
    mostra_linha()
    print(f'{titulo:^40}')
    mostra_linha()

titulo_personalizado('Sistema de Alunos')
titulo_personalizado('Carlos Vieira')
titulo_personalizado('Dandara Fonseca Vieira')
pula_trexos()


# FUNÇÃO SOMA PARAMETROS ----------------------------------------------------
def soma_valores(a, b):
    s = a + b
    print(s)

soma_valores(15, 10)
soma_valores(10, 10)
soma_valores(5, 2)
pula_trexos()


# DEIXANDO PARAMETROS EXPLICITOS ----------------------------------------------------
def soma2(a, b):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma da A + B = {soma}')

soma2(b=5, a=4)
pula_trexos()


# EMPACOTAR PARAMENTROS TUPLAS ----------------------------------------------------
def contador(* numeros):  # cria uma tupla com todos os valores
    for valor in numeros:
        print(f'{valor} ', end='')
    print('FIM!')

contador(2, 8, 9, 6, 7)
contador(3, 8)
contador(7, 1, 9, 3)
pula_trexos()


# FUNÇÕES COM LISTAS ----------------------------------------------------
def dobra_valores(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
    print(f'Valores dobrados da lista: {lista}')

lista_numeros = [7, 5, 8, 3]
print(f'Valores padrão da lista: {lista_numeros}')
dobra_valores(lista_numeros)
pula_trexos()


# FUNÇÕES COM QUANTIDADE DE PARAMETROS SEM LIMITES ------------------------------------------------
def soma_valores_1(* valores):
    s = 0
    for numero in valores:
        s += numero
    print(f'Somando os valores {valores} temos {s}')

soma_valores_1(2)
soma_valores_1(2, 8, 10)
soma_valores_1(5, 7)

