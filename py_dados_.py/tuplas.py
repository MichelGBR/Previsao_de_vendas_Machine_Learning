#tupla é uma variável no qual nao pode mudar

lista1 = [1, 2, 6, 9]

#lista1 [0] = 88 #substituir o indice
#print(lista1)

del lista1 [3] #comando para remover algo da lista
print (lista1)


tupla = (0 , 3 , 5 , 8) #utilizamos parênteses e não há como mudar algo nela

nova_tupla = tuple(lista1)
print(nova_tupla)

#importante para a tupla é quando não queremos que um valor mude



