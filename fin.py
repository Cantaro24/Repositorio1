contador = 0
suma = 0
while True:
    numero = input ("Introduzca un numero = ")
    if (numero == "Fin"):
        break
    contador = contador + 1
    suma = suma + int(numero)
    print("contador", contador)
    print("suma", suma)
    print("promedio", suma/contador) 