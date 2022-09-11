'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''

'''
# minha solução
from random import randint

computador = randint(0, 10)
jogador = int(input('Digite um número de 1 a 10: '))
tentativas = 1

while jogador != computador:
    jogador = int(input('Você errou! Tente novamente: '))
    tentativas += 1
    if jogador == computador:
        print('Você ganhou!!!')

print('Você precisou de {} para vencer!'.format(tentativas))
'''
# solução do professor
from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número  entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente: ')
        elif jogador > computador:
            print('Menos... Tente novamente: ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
