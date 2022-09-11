'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

dimensao = largura * altura
tinta = dimensao / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(largura, altura, dimensao))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))