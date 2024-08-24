'''
opcion = "0"

opciones = ["1", "2", "3"]

while not opcion in opciones:
    input("Introduzca su opción: ")

q

print("Continuamos con el programa.") 
'''


password = ""

password_bd = "123456"

limite_intentos = 3
intentos = 0

while password != password_bd:
    password = input("Ingrese el passoword correcto: ")
    intentos += 1

    if intentos == limite_intentos:
        print("Usted ha sido bloqueado del sistema")
        break

print("continuamos con el programa")