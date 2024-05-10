#criando funcoes

def numero_multi(a, b):
    soma_multi = a * b
    print (soma_multi)
    return soma_multi
    
numero_multi(3,5)

#lambda é uma forma resumida de criar uma funcao

numero_multi2 = lambda a, b : a * b
numero_multi2(3,5)

print(numero_multi2(3,5))

#outro exemplo

x = lambda f : f/2
print(x(12))

