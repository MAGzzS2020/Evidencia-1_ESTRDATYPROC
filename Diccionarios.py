'''
-Es una lista de pares de elementos con estructura clave:valor
-No se accesa a los elementos por posicion, sino por el valor de su clave
-Se delimita entre llaves {}
-A un diccionario se le refiere tambien como dict
'''


#Creacion de diccionarios
diccionario_vacio = {}
diccionaro_citas = {"T'Challa":"Wakanda Forever",
                    "Thanos":"The hardest choices require the strongest wills",
                    "AMLO":"Me canso ganso"}
print(diccionaro_citas)
pass


#Accesar elementos
print(diccionaro_citas["Thanos"])
pass


#Agregar elementos: Se agrega la nueva llave y se indica su valor
print("*" * 20)
diccionaro_citas["Plankton"] = "¡Por fin tengo la formula de la cangreburger"
print(diccionaro_citas)
pass


#Eliminar elementos de un diccionario
print("*" * 20)
del diccionaro_citas["AMLO"]
print(diccionaro_citas)
pass
#Opciones para obtener el volcado de un diccionario
#en cada una, la respuesta DEBE convertirse en una lista primero
#para un mas facil manejo


#Opcion 1: Todas las claves, solamente las claves
print(list(diccionaro_citas.keys()))
pass


#Opcion 2 : Todos los valores, solamente los valores
print(list(diccionaro_citas.values()))



#Opcion 3 : Todos los elementos, elementos por elementos
print(list(diccionaro_citas.items()))

