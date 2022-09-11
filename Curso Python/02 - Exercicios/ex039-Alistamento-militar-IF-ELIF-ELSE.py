'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

print('Selecione o seu sexo:')
print('[ 1 ] Sexo MASCULINO')
print('[ 2 ] Sexo Feminino')
sexo = int(input('Digite a opção: '))


if sexo == 1:
    nasc = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc

    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))

    if idade < 18:
        print('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(ano + (18 - idade)))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(nasc + 18))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo == 2:
    print('Pessoas do sexo FEMININO não precisam se alistar.')
else:
    print('Opção inválida. Tente novamente.')
