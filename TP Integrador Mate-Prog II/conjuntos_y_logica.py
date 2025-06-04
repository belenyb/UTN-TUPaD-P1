# Definimos los conjuntos con los numeros de DNI de cada alumno

A = {3, 4, 5, 9}
B = {2, 3, 4, 7, 9}
C = {0, 2, 4, 5, 6, 8, 9}
D = {1, 2, 4, 8, 9}


# Escribimos la primer expresion:

"""" Un número pertenece al conjunto B pero no al conjunto C."""

# Se hace la resta de los elementos de los conjuntos B - C

resultado = B - C
print("Resultado:", resultado) # Respuesta esperada: {3,7}

#-----------------------------------------------------------------------------------------------------------------

# Escribimos la segunda expresion:
"""" Un número pertenece tanto al conjunto C como al conjunto D, pero no pertenece al conjunto A."""

# La operación C & D devuelve los elementos que están al mismo tiempo en C y en D pero no en A.
# por lo tanto primero se realiza la interseccion entre C y D, y luego al resultado se lo resta el conjunto A.

resultado = (C & D) - A
print("Resultado:", resultado) # Restultado esperado {2,8}

#------------------------------------------------------------------------------------------------------------------
