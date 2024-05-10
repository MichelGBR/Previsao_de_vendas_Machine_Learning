
#Definindo as variáveis e seus cálculos
salario1 = (int(input("Digite o salário do funcionário : ")))
salario_menor_999 = salario1 * 0.10
salario_maior_1000 = salario1 * 0.08

#coloquei as possibilidades representadas por 'if' ou 'elif'
#fiz o cálculo de porcentagens, sendo uma 0.10 (10% , menor que 1000) e 0.08 (8%, maior que 1000)

if salario1 <= 999: #aqui, decidi botar um valor menor que 1000 (999) para não gerar conflito caso
# o salário seja exatamente 1000
    
    salario_menor_999
    print('O funcionário vai receber um aumento de ' , salario_menor_999 ,'reais,' "totalizando" ,
          salario1 + salario_menor_999 ,'como seu novo valor para receber ao mês' )
    
elif salario1 >= 1000 : 
    
    salario_maior_1000
    print('O funcionário vai receber um aumento de ' , salario_maior_1000 ,'reais,' "totalizando" ,
          salario1 + salario_maior_1000 ,'como seu novo valor para receber ao mês' )
