# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("1)", precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("2)", precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

nombres_frutas = list(precios_frutas.keys())
print("3)", nombres_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contador = 5
numero_consulta = 0
numeros_telefonicos = {}

while numero_consulta < contador:
    clave = input("Ingrese nombre de contacto: ")
    valor = input("Ingrese número de teléfono: ")
    numeros_telefonicos[clave] = valor
    numero_consulta += 1

nombre_a_buscar = input("Ingrese el contacto a consultar: ")
if nombre_a_buscar in numeros_telefonicos:
    print(numeros_telefonicos[nombre_a_buscar])
else:
    print("El contacto no se encuentra registrado.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Conteo de palabras:", contador)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de notas de {nombre}: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1_aprobados = {"Martin", "Luciana", "Esteban", "Marta"}
parcial_2_aprobados = {"Martin", "Luciana"}

interseccion = parcial_1_aprobados & parcial_2_aprobados
print("Aprobaron ambos parciales:", interseccion)

diferencia = parcial_1_aprobados ^ parcial_2_aprobados
print("Aprobaron solo uno de los dos parciales:", diferencia)

union = parcial_1_aprobados | parcial_2_aprobados
print("Total de estudiantes que aprobaron al menos un parcial: ", union)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

dict_productos = {"telefono": 10, "computadora": 25, "monitor": 3}
consulta_usuario = input("Ingrese producto para consultar stock: ")
if consulta_usuario in dict_productos:
    print(f"El stock de {consulta_usuario} es: {dict_productos[consulta_usuario]}")
    segunda_consulta = input("Desea agregar unidades al stock? (s/n): ")
    if segunda_consulta == "s":
        nuevo_stock = int(input("Ingrese cuantas unidades desea agregar: "))
        dict_productos[consulta_usuario] = dict_productos[consulta_usuario] + nuevo_stock
    else:
        exit
else:
    stock_nuevo_producto = int(input("El producto no existe, por favor ingrese su stock para agregarlo: "))
    dict_productos[consulta_usuario] = stock_nuevo_producto

print(dict_productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Programación 1",
    ("martes", "14:00"): "Matemática",
    ("miercoles", "16:00"): "Organización Empresarial",
    ("jueves", "11:00"): "Arquitectura y Sistemas Operativos"
}

dia = input("Ingresá el día en minúsculas (ej: lunes): ")
hora = input("Ingresá la hora en formato HH:mm (ej: 10:00): ")

evento = agenda.get((dia, hora))

if evento:
    print(f"El {dia} a las {hora} hay clase de: {evento}")
else:
    print(f"No hay ninguna clase agendada para el {dia} a las {hora}.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Japón": "Tokio"
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
