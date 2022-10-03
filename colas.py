"""
Implementacion de colas mediamte listas y deque()
Demuestra las diferencias en la forma de implementacion 

"""
from tkinter import SEPARATOR


SEPERADOR = ("*" * 20) + "\n"

cola =  list()  #Coloca utilizando una lista 

for cantidad in range(5):
    nuevo = input("Nombre del recien llegado: ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos:")
for elemento in cola:
    print(elemento)
print(SEPARATOR)
pass

print("Procedemos a retiralos de la cola")
while cola:
    print(cola.pop(0))
pass #Vereficar que la estructura se encuentre vacia
