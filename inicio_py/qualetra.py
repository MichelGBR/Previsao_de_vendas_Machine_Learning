frase = 'Eu tenho certeza que serei Cientista de Dados e a Giovanna a melhor Arquieta do mundo.'.lower()

# para saber qual letra mais aparece em uma frase utilizamos o comando "print (frase.count)"

variavel = 0

while variavel < len(frase):
    letra_atual = frase [variavel]
    qnts_apareceu = frase.count (letra_atual)

    print(letra_atual , qnts_apareceu)
    variavel += 1