#fiz a técnica no qual a pessoa tem que digitar um número de 0 até 10
#o contrário disso vai aparecer uma mensagem avisando que não está correto

dig_0_10 = int(input("Digite um número de 0 até 10:"))

if dig_0_10 <= 10:
    print("Você digitou o número " , dig_0_10,"," " está correto com o que pedimos!")

else:
    print("Você não digitou um número que esteja entre 0 a 10")