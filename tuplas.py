# Acceder a elementos - Tupla[0]

lenguajes = ("javascript", "java", "python")

print(type(lenguajes))

# rupla tiene 2 métodos count e index

print(lenguajes.count("java"))

# Acceder a elemntos -> tupla[0]
# Cortar tuplas -> tupla[0:3]
print(lenguajes[1:3])

# Convertir tuplas a listas.
lenguajes = ("javascript", "java", "python", "go")
lenguajes = list(lenguajes)

#Convertir lista a tupla
lenguajes[1] = "JAVA"
lenguajes = tuple(lenguajes)
print(type(lenguajes))
print(lenguajes)

# Comprobar si un elemento se encuentra en la tupla
lenguajes = ("javascript", "java", "python", "go")

print(lenguajes.count("go")) # 
print("go" in lenguajes)   # Este método de comprobación me da una respuesta booleana True/False

# Ejemplo:
if "C#" in lenguajes:
    pass

# Unir tuplas
# Extend no sirve porque una tupla es un elemnto inmutable y con extend lo estaríamos modificand
lenguajes1 = ("javascript", "java", "python", "go")
lenguajes2 = tuple("C#") # si una función tiene un solo elemnto, hay que ocupar tuple o ponerle una coma al final para convertirlo en tuple, ya que con un solo elemnto no lo reconoce como tupla

print(type(lenguajes1))
print(type(lenguajes2))

lenguajes = lenguajes1 + lenguajes2

print(lenguajes)


# Eliminar tuplas
lenguajes1 = ("javascript", "java", "python", "go")
print(lenguajes)
del lenguajes
print(lenguajes) # Esto da error porque estamos tratando de acceder a elemntos que ya no existen