# ---------- STRINGS ----------
# alinhar no centro
print(f'{"LISTAGEM DE PREÇOS":^40}')

# ---------- WHILE ----------
# pedir para continuar ou não
while True:
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

# ---------- LISTAS ----------
# append('') adiciona novo elemento no final da lista