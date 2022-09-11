'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

m = float(input('Digite a metragem: '))

cm = m*100
mm = m*1000

print('A conversão de {} metros em centimetros é {}cm. e em milimetros é {}mm'.format(m, cm, mm))
