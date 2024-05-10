#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.
"""

"""
#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".



digitar_numero = float(input("Digite um numero inteiro"))
numero_par = digitar_numero % 2


if digitar_numero:
    print(f'o seu numero inteiro é {digitar_numero}')
    
    if numero_par == 0:
        print (f'O seu numero é par!')
    else:
        print("o seu numero é impar")
        
else:
    print('o seu numero não é inteiro')    



"""
"""""""
que_horas_sao = float(input("Que horas sao agora?"))

manha = que_horas_sao 
tarde = que_horas_sao 
noite = que_horas_sao 

if manha >= 0 and manha <=11:
    print("Bom dia!")

elif tarde >= 12 and tarde <= 18:
    print("Boa tarde")

elif noite >= 19 and noite <= 23:
    print("Boa noite!")

else:
    print("Você nao digitou nada")
"""
  

 #Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

"""
nome_da_pessoa = input("Digite o seu primeiro nome: ")

tamanho_nome = len(nome_da_pessoa)

if tamanho_nome <= 4:
    print(f'seu nome {nome_da_pessoa} é curto')

elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print(f'seu nome {nome_da_pessoa} é normal')

elif tamanho_nome >= 6 and tamanho_nome <= 15:
    print(f'seu nome {nome_da_pessoa} é grande')

"""         