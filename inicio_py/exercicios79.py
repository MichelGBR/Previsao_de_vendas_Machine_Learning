""""Exercício
Peça ao usuário para digitar seu nome1
Peça ao usuário para digitar sua idade1
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}1
        Seu nome invertido é {nome invertido}1
        Seu nome contém (ou não) espaços1
        Seu nome tem {n} letras1
        A primeira letra do seu nome é {letra}1
        A última letra do seu nome é {letra}1
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."1
"""

nome_de_usu = input("Digite seu nome: ")
idade1 = input("Digite sua idade: ")
if nome_de_usu and idade1 :
    print(f"Seu nome é {nome_de_usu}")


    if " " in nome_de_usu:
        print("Você tem espaco em seu nome")

    else:
        print("Você não tem espaco em seu nome")

    print(f"O numero de caracteres em seu nome é {len(nome_de_usu)} ")
    print(f'A primeira letra do seu nome é: {nome_de_usu[0]}')
    print(f"a última letra de seu nome é: {nome_de_usu[-1]}")
    print(f"Seu nome invertido é: {nome_de_usu[::-1]}")

else:
    print("Você não digitou nada")

    print('Eu vou CONSEGUIR')    

 




