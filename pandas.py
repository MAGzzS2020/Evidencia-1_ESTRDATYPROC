from operator import index
import numpy as np
import pandas as pd

SEPARADOR = ("*" * 20) + "\n"

#Crear una serie con valores iniciales 
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(notas)
print(SEPARADOR)



#Crear una serie de 6 elementos que tengan el mismo valor
iguales = pd.Series(100, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)



#Estadisticas Descriptivas para una serie
print("notas :")
print(f"{notas}")
print(f"cantidad = {notas.count()}")
print(f"media = {notas.mean()}")
print(f"minimo = {notas.min()}")
print(f"maximo = {notas.max()}")
print(f"desviacion standard = {notas.std()}")
print("Sumarizacion descriptiva:")
print(notas.describe())
print(SEPARADOR)


#Derie con imdices personalizados
print("Series con indices personalizados:")
notas_asignadas = pd.series([87, 100, 85, 60, 78], index=["Cresencio", "Domitila", "Rutilio", "Panfilo", "Ludoviko"])

print(notas_asignadas)
print(SEPARADOR)




print("Serie generada a partir de un diccionario")
notas_asignadas_dict = pd.Series({"Cresencio":87, "Domitila":100, "Rutilio":85, "Panfilo":60, "Ludoviko":78})

print(notas_asignadas_dict)
print(SEPARADOR)
