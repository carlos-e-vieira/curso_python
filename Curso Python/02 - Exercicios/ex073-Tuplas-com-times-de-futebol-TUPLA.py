'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Santos.
'''

times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Inter', 'Atlético-MG',
         'América-MG', 'Red Bull Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará',
         'Fortaleza', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')

print('=-'*30)
print(f'Lista de times do Brasileirão: {times}')
print('=-'*30)
print(f'Os 5 primeiros são {times[0:5]}')
print('=-'*30)
print(f'Os 4 últimos são {times[-4:]}')
print('=-'*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-'*30)
print(f'O Santos está na {times.index("Santos") + 1} posição.')
