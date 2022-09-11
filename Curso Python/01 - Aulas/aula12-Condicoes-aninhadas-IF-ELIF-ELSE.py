nome = str(input('Digite seu nome: '))

if nome == 'Carlos':
    print('Que nome lindo!')
elif nome == 'Dandara':
    print('Nome de rainha :)')
elif nome == 'Rosa' or nome == 'Geiza' or nome == 'Li' or nome == 'Giovanna':
    print('Conheço uma pessoa com o nome igual ao seu.')
elif nome in 'Bianca Fernanda Renata':
    print('Minha prima tem o mesmo nome que o seu!')
else:
    print('Nome + ou -')
print('Tenha um bom dia \033[31m{}\033[m!'.format(nome))