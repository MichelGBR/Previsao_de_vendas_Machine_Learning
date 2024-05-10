#é um resumo do for i in 


kph = [40, 50, 10, 11]

mph = list(map(lambda x : x/1.61, kph)) #smp separar com ,

print(mph)


mph2 = [x/1.61 for x in kph] # a melhor forma e mais resumida!
print(mph2)



carac = [i +"x" for i in "Michel" ]
print(carac)

#list cpmprehension
