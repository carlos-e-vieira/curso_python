'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

# minha solução
from time import sleep

sair = 0

n1 = int(input('Primeiro valos: '))
n2 = int(input('Segundo valor: '))

while sair != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qua é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valos: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        sair = 5
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Finalizando...')
sleep(2)
print('Fim do programa! Volte sempre!')
