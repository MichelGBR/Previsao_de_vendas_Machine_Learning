#lista1 = [1 , 2 , 3]


#print(lista1[1]) #python comeca com 0, aqui eu botei o numero de indice + print


#lista2 = [[3 , 2 , 4] , [5 , 8 , 7]]
#print(lista2[0][1]) #lista dentro de lista

import random #funcao random é responsável por sortear algo
cidades = ["SP" , "RJ" , "MG" , "SC"]
escolher = random.choice(cidades)
print(f"A cidade escolhida foi {escolher}")

a = [1 , 2 , 3] #a funcao append serve pra add algo na lista em seu final
a.append (79)
print(a)

b = [1, 3 , 44, 33]

for i in b: #metodo para juntar as listas
    a.append(i)

    print(a)