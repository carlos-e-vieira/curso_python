maior = 0
menor = 0

for c in range(1, 4):
    num = int(input('Digite o {}º valor: '.format(c)))
    if c == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))

