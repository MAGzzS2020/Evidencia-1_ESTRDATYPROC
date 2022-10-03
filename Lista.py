"""
Ejemplo para demosrar el manejo de letras 
Demuestra: Creacion, acceso a elementos, oredenamiento y comprencion de listas
"""

SEPARADOR =  ("*" * 20) + "\n"

#Creacion de listas
#Lista vacia
lista_vacia = list()
otra_lista_vacia = []
#Lista con elementos iniciales
lista_uno =[1, 2, 3, 4]
print(lista_uno)
print(SEPARADOR)
pass

#Agregar elementos a listas existentes 
lista_uno.append(5)
print(lista_uno)
lista_uno.append((6, 7)) #una lista puede ser un elemento de otra lista
print(SEPARADOR)
pass



#Remover elementos de una lista
lista_uno.remove((6, 7)) #se le pasa el valor del elemento a remover
print(lista_uno)
print(SEPARADOR)
pass


#Ordenar elementos de una lista 
#Sort()
lista_original1 = [3, 4, 2]
print(lista_original1)
lista_original1.sort()
print(lista_original1)
pass



#Sorted()
lista_original2 = [23, 10, 30, 5]
lista_ordenada = sorted(lista_original2)
print(f"lista original = {lista_original2}, y la vercion ordenada es {lista_ordenada}")
print(SEPARADOR)
pass



#Comprencion de listas
print(f"lista original = {lista_uno}")

#Sin comprension de listas
lista_uno_al_doble =[]
for valor in lista_uno:
    lista_uno_al_doble.append(valor * 2)
print(f"lista resultante, cada elemento al doble = {lista_uno_al_doble}")
pass

#Con comnprencion de listas
lista_uno_al_doble = [valor * 2 for valor in lista_uno]
print(f"Mismo resultado, pero con comprension de listas = {lista_uno_al_doble}")
pass

#Comprension de listas con condicion 
lista_valores_pares = [valor for valor in lista_uno if (valor % 2 == 0)]
print(f"Solamente se agregaron los elementos con valor par: {lista_valores_pares}")
