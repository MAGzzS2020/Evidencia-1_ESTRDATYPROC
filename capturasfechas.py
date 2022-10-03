import datetime 
SEPARADOR = "*" * 30
#Se desea capturar una lista de fichas de nacimiento (3) y se debera informar cuantos 
#años cumple esas personas en el año en curso.


lista_fechas = []
for elemento in range(3):
    fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
    fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
    lista_fechas.append(fecha_procesada)

print(SEPARADOR)

lista_edades = [datetime.date.today().year - fecha.year for fecha in lista_fechas]

print(lista_edades)
