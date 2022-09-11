"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'grátis', 'lista', 'tupla', 'python', 'java', 'javascript', 'php', 'mysql')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')

