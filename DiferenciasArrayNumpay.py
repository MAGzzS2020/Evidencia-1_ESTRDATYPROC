import numpy as np
import random
SEPARADOR = ("*" * 20) + "\n"

#Comprobacion de que array de numpy y una lista no posee el mismo comportamiento:
#Una lista puede contener elementos de diferentes tipos de dato
#en una array de numpy todos los elementos son del mismo tipo de dato

lista = [10, "abc", 20]
print(lista)
print([type](elemento) for elemento in lista)
print(SEPARADOR)


#Si se le proporciona un elemento de un tipo de dato diferente, numpy buscara
#Integrar los valores a un tipo "neutro" que los pueda abarcar (usualmente str)
arreglo = np.array([10, "abc", 20])
print(arreglo)
print([type(elemento) for elemento in arreglo])
print(SEPARADOR)

#Una lista no ofrece operaciones de algebra matricial, por ejemplo:
#La multiplicacion de un array o matriz por un escalar, o por una matriz compatible
lista = [10, 15, 20, 25]
print(lista)
print(lista * 2)
print(SEPARADOR)

arreglo = np.array([10, 15, 20, 25])
print(arreglo)
print(arreglo * 2)
print(SEPARADOR)

matrizA = np.array([[random.randrange(300) for valor in range(10) for valor in range(5)]])
matrizB =np.array([[random.randrange(300) for valor in range(10) for valor in range(5)]])

print(f"matriz A\n{matrizA}")
print("\nX\n")
print(f"matriz B\n{matrizB}")
print("\n=\n")
print(matrizA * matrizB)
