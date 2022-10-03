import math
SEPARADOR = ("*" * 20) + "\n"
"""
Ejemplo para ilustrar  la importacion de la libreria math en Python 3
Demuestra el uso de: floor(x), trunc(x),ceil(x),round(x),factorial(x),pow(x,y),sqrt(x) y pi
"""

valorflotante = float(input("Introduce un valor con fraccion decimal:\n"))
print(f"El siguiente entero hacia arriba de {valorflotante} es {math.ceil(valorflotante)}")
print(SEPARADOR)
print(f"El siguiente entero hacia abajo de {valorflotante} es {math.floor(valorflotante)}")
print(SEPARADOR)
print(f"La parte entera truncada de {valorflotante} es {math.trunc(valorflotante)}") #Equivalente a floor() para positivos, y a ceil() para negativos porque se mueve hacia el 0
print(SEPARADOR * 2)
pass
valornumerico = int(input("Dame un valor entero:\n"))
print(f"La raiz cuadrada de {valornumerico} es igual {math.sqrt(valornumerico)}")
print(SEPARADOR)
print(f"El factorial de {valornumerico} es igual a {math.factorial(valornumerico)}")
potencia = int(input("Dame un valor entero:\n"))
print(f"El resultado de elevar {valornumerico} a la {potencia} potencia es igual a {math.pow(valornumerico,potencia)}")
print(SEPARADOR * 2)
pass
