import numpy as np
import random
SEPARADOR = ("*" * 20) + "\n"

#menores a 5
arreglo_uni = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arreglo_uni)
print(SEPARADOR)

print(f"Valores menores a cinco en {arreglo_uni}")
filtro_menores_a_5 = arreglo_uni < 5
print(filtro_menores_a_5)
print(SEPARADOR)

menores_a_5 = arreglo_uni[filtro_menores_a_5]
#menores_a_5 = arreglo_uni[arreglo_uni < 5] Forma de abrviar
print(menores_a_5)
print(SEPARADOR)

#Filtrado booleano sobre una matriz
matriz = np.array([[random.randrange(300) for valor in range(10)] for valor in range(5)])
print(matriz)
print(SEPARADOR)
#
print("Valores menores a 200 eb la matriz")
filtro_menores_a_200 = matriz < 200
print(filtro_menores_a_200)

menores_200 = matriz[filtro_menores_a_200]
print()
print(menores_200)

#Filtrado booleano compuesto sobre una matriz
#Tip: se generan dos mapas binarios y se conbinan con & (AND binario) o con | (OR bianrio) segun se requiera
print("Valor menores a 200 a 200 en la matriz y que sean pares ")
filtro_pares_menores_a_200 = (matriz < 200) & (matriz % 2 == 0)
print(filtro_pares_menores_a_200)

pares_menores_200 = matriz[filtro_pares_menores_a_200]
print()
print(pares_menores_200)
