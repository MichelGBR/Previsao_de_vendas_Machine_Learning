palavra = "cassio"
letras_acertadas = ""
numeros_tentativas = 0

import os

while True:

    digitar = input("Digite apenas uma letra: ")
    numeros_tentativas += 1


    if len(digitar) > 1:
        print("Digite apenas uma letra!")
        continue
    
    if digitar in palavra :
        letras_acertadas += digitar

    palavra_formada = ""
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:     
                palavra_formada += letra_secreta 

        else:
            palavra_formada += "*"
        
    print('A Palavra formada:' , palavra_formada)

    if palavra_formada == palavra:
            
        os.system('cls')
            
        print("Parabéns!! você acertou a palavra secreta! ;o")
        print(f'A palavra secreta era: ' , palavra_formada)
        print('Voce acertou com :' , numeros_tentativas , "tentativas")
        letras_acertadas = ""
        numeros_tentativas = 0




