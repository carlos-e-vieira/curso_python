frase = 'Curso em Vídeo Python'
frase2 = '   Curso em Vídeo Aulas Youtube        '

print('='*20)
print('string[2] -> Imprindo um indice da string: ', frase[2])

print('='*20)
print('string[::2] -> Do inicio ao fim pulando de 2 wm 2: ', frase[::2])

print('='*20)
print('string.count("o") -> Conta quantas vezes tem a letra passada no parâmetro: ', frase.count('o'))

print('='*20)
print('string.upper().count("O") -> Transforma tudo em maiúscculo e conta o caracter passado no parâmetro: ', frase.upper().count('O'))

print('='*20)
print('len(string) -> Conta a quantidade de caracters da string: ', len(frase))

print('='*20)
print('string.strip() -> Remove todos os espaços em branco: ', frase2.strip())

print('='*20)
print('string.replace("P1", "P2") -> Substitui o primeiro parâmetro da string pelo segundo parâmetro: ', frase.replace('Curso', 'Treinamento'))

print('='*20)
print('"Curso" in frase -> Verifica se a palavra está dentro da string retornando True ou False: ', 'Curso' in frase)

print('='*20)
palavras = frase.split()
print('string.split() -> Transforma uma string em array, separados por espaço: ', palavras[2])
