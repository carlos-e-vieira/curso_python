n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#\n é quebra de linha no print
#:.3f define que o numero seja float com o limite de 3 caracteres depois do .
#end=' ' tira a quebra de linha de um print para outro

print('A soma é {}, o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))