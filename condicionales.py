valor = True

if valor:
    print("Es verdadero")
else:
    print("Es falso")

valor = 0

if valor:
    print("Es verdadero")
else:
    print("Es falso")


# Cuando las listas están vacias son falsas
valor = []

print(type(valor))
if valor:
    print("Es verdadero")
else:
    print("Es falso")

# Cuando un string está vacio es falso
valor = ""

print(type(valor))
if valor:
    print("Es verdadero")
else:
    print("Es falso")

# Esto por ejemplo sirve para menus 

elementos = [1,2,3,4,5]

valor = int(input("Ingrese un valor: "))
if valor in elementos:
    print("Opción válida")
else:
    print("Opción no válida")

#O

elementos = [1,2,3,4,5]

opcion = int(input("Ingrese un valor: "))
if opcion in elementos:
    if opcion == 1:
        print("Ha elegido la opción número 1")
    elif opcion == 2:
        print("Ha elegido la opción número 2")
    elif opcion == 3:
        print("Ha elegido la opción número 3")
else:
    print("Opción no válida")


# *not*
if not False:
    print("Es falso")

valor = True
if valor:
    print("Es verdadero")
else:
    print("No es falso")


# REQUISITOS PARA APROBAR EL CURSO (EJERCICIO PRÁCTICO IF y AND)
'''
asistencia_req = 75
promedio_req = 60
trabajos_req = 8

asistencia = 80
promedio = 65
trabajos = 8


if asistencia >= asistencia_req and promedio >= promedio_req and trabajos >= trabajos_req:
    print("cumple")
else:
    print("no cumple")
'''

asistencia_req = 75
promedio_req = 60
trabajos_req = 8

asistencia = 80
promedio = 65
trabajos = 8

a_asistencia = asistencia >= asistencia_req
a_promedio = promedio >= promedio_req
a_trabajo = trabajos >= trabajos_req

if a_asistencia and a_promedio and a_trabajo:
    print("Cumple")
else:
    print("no cumple")


# short hand (forma corta del if)
valor = 5
print("Es verdadero") if valor >=0 else print("Es falso")