'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 parta viagens mais longas.
'''

viagem = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))

preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))


'''if viagem <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.45))'''