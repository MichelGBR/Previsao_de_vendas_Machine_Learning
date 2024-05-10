#utilizamos {} para representar

#dicionario = {chave:valor}
#chave: curso "palavra de pesquisa"
#valor: Python ML "resposta"

dicionario = {"Curso" : "Python ML",
               "Produtor" : "Michel"
                , "Pagar" : "90 reais"
                 , "Nota" : 10 }

print(dicionario ["Nota"] )

dicionario ["Produtor"] = "Giovanna" #substituindo

print(dicionario)

dicionario ["Pré requisito"] = "Estudar" #substituindo

print(dicionario)

# para descobrir as chaves é só fazer o comando "dicionario.keys"

print(dicionario.keys())

# para descobrir os valores é só usar dicionario.values
# para descobrir ambos é só usar dicionario.itens