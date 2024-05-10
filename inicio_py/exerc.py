#valor1 = input("Digite o primeiro valor: ")
#alor2 = input("Digite o segundo valor: ")

#if valor1 > valor2 :
 #   print(f'O {valor1} é maior que o {valor2} ')

#elif valor2 > valor1 :
 #   print(f'O {valor2} é maior que o {valor1} ')



nomedeusu = input("Digite [e]ntrar ou [s]air ")
senhalogin = input("Digite a senha ")

senha = '123456'


if nomedeusu == 'e' and senhalogin == senha:
    print("Você acertou sua senha")

else:
    print("Senha incorreta")


    numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')