'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS CARLOS '))
total = float(input('Preço da compras? R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    desconto = (10 * total) / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(total, total - desconto))
elif opcao == 2:
    desconto = (5 * total) / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(total, total - desconto))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(total / 2))
elif opcao == 4:
    parcelas = int(input('Quantidade de parcelas? '))
    juros = (20 * total) / 100
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, (total + juros) / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(total, total + juros))
else:
    print('Opção inválida. Tente novamente.')
