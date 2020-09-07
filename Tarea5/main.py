prueba1 = "_servidor1"
prueba2 = "3servidor"
abecedario = ["a", "b" ,"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digitos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def afd(entrada):
    letrasAFD = []
    contador_fase = 0
    contador_letra = 0
    for letter in entrada:
        letrasAFD.append(letter)

    if letrasAFD[contador_letra] == "_":
        contador_letra = contador_letra+1
        while contador_fase != 4:
            letra = abecedario.count(letrasAFD[contador_letra])
            if letra >= 1:
                contador_letra = contador_letra +1
            elif letra == 0 and (digitos.count(letrasAFD[contador_letra])):
                contador_fase = 4
                print("CADENA ACEPTADA  %s" %entrada)
            else:
                print("CADENA NO VALIDA  %s" %entrada)
                break
    else:
        print("CADENA NO VALIDA  %s" %entrada)


afd(prueba1)
afd(prueba2)
