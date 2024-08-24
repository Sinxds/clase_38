conjunto = set({2, 3, 4})  # Para evitar confución con los diccionarios al estar vacios, es mejor utilizar la función "set()"

print(type(conjunto))

# Longitud de un set

conjunto = set({2, 3, 4})

print(len(conjunto))

# Comprobante de un elemento

print(6 in conjunto)

# Agregar elementos -> add()
# En las listas es append()
conjunto = set({1, 2, 3, 4, 5})
conjunto.add(6)
#O
conjunto = set({1, 2, 3, 4, 5})
nuevo_valor = input("Agrega un nuevo valor")
conjunto.add(nuevo_valor)
# O
conjunto = set({1, 2, 3, 4, 5})
conjunto.add(int(input("Agrega un nuevo valor")))
print(conjunto)

# Eliminar elementos -> remove()
# si el elemento no está presente en el conjunto, nos va a dar un error tipo "Key error"
conjunto.remove(2)
print(conjunto)

# Agregar varios elementos -> Update
conjunto = set({1, 2, 3, 4, 5})
conjunto.update([6, 7, 8, 9])
conjunto.update([2, 5, 8, 9, 10]) # Valores duplicados se suprimen (no los agrega)
print(conjunto)

# Remover de forma aleatoria -> pop()
conjunto = set({1, 2, 3, 4, 5})
conjunto.pop()

print(conjunto)

#limpiar o vaciar conjunto -> clear()

conjunto = set({1, 2, 3, 4, 5})
conjunto.clear()
print(conjunto)

# Unir conjuntos -> union()
conjunto1 = set({1, 2, 3, 4, 5})
conjunto2 = set({6, 7, 8, 9, 10})
conjuntos = conjunto1.union(conjunto2)
# Esto no modificará el conjunto1

print(conjuntos)

# Intersección de elementos entre tuplas -> intersection()

conjunto1 = set({1, 5, 7}) # hace match (en este caso devolverá el 5)
conjunto2 = set({2, 5, 9})

interseccion = conjunto.intersection(conjunto2)

print(interseccion)

# Diferencias
conjunto1 = set({1, 5, 7, 2}) # Muestra como resultado un valor que no esté en los conjuntos en este caso 7 y 2
conjunto2 = set({2, 5, 9})

diferentes = conjunto1.difference(conjunto2)
print(diferentes)