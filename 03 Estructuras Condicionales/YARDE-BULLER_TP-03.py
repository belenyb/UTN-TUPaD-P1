# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
age = int(input("Ingrese su edad: "))
if (age > 18):
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
grade = int(input("Ingrese su nota: "))
if (grade >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
number = int(input("Ingrese un número: "))
if (number%2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
age = int(input("Ingrese su edad: "))
if (age < 12):
    print("Niño/a")
elif (age >= 12 and age < 18):
    print("Adolescente")
elif (age >= 18 and age < 30):
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
password = input("Ingrese una contraseña: ")
passwordLength = len(password)
if (passwordLength >= 8 and passwordLength <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print({media, mediana, moda})
print((media > mediana) and (mediana > moda))
print((media < mediana) and (mediana < moda))
print((media == mediana and mediana == moda))

if (media > mediana) and (mediana > moda):
    print("Hay sesgo positivo o a la derecha")
elif (media < mediana) and (mediana < moda):
    print("Hay sesgo negativo o a la izquierda")
elif (media == mediana and mediana == moda):
    print("Sin sesgo")
else:
    print("No se pudo determinar el sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
word = input("Ingrese una palabra: ")
if (word[-1].lower() == "a" or word[-1].lower() == "e" or word[-1].lower() == "i" or word[-1].lower() == "o" or word[-1].lower() == "u"):
    print(f"{word}!")
else:
    print(word)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
name = input("Ingrese su nombre: ")
option_number = int(input("Ingrese 1 > si quiere su nombre en mayúsculas, 2 > si quiere su nombre en minúsculas o 3 > si quiere su nombre con la primera letra mayúscula"))
if (option_number == 1):
    print(name.upper())
elif (option_number == 2):
    print(name.lower())
elif (option_number == 3):
    print(name.title())
else:
    pass

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitude = float(input("Ingrese la magnitud del terremoto: "))
if (magnitude < 3):
    print("Muy leve")
elif (magnitude >= 3 and magnitude < 4):
    print("Leve")
elif (magnitude >= 4 and magnitude < 5):
    print("Moderado")
elif (magnitude >= 5 and magnitude < 6):
    print("Fuerte")
elif (magnitude >= 6 and magnitude < 7):
    print("Muy Fuerte")
elif (magnitude >= 7):
    print("Extremo")
else:
    pass

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisphere = input("En qué hemisferio se encuentra? N/S: ").upper()
current_day = int(input("Ingrese el corriente numero de día: "))
current_month = int(input("Ingrese el corriente numero de mes: "))
current_date = (current_month, current_day)

if (hemisphere == "N"):
    if (current_day >= 21 and current_month == 12) or current_month == 1 or current_month == 2 or (current_month == 3 and current_day <= 20):
        print("Es invierno")
    elif (current_month == 3 and current_day >= 21) or current_month == 4 or current_month == 5 or (current_month == 6 and current_day <= 20):
        print("Es primavera")
    elif (current_month == 6 and current_day >= 21) or current_month == 7 or current_month == 8 or (current_month == 9 and current_day <= 20):
        print("Es verano")
    elif (current_month == 9 and current_day >= 21) or current_month == 10 or current_month == 11 or (current_month == 12 and current_day <= 20):
        print("Es otoño")

elif hemisphere == "S":
    if (current_month == 6 and current_day >= 21) or current_month == 7 or current_month == 8 or (current_month == 9 and current_day <= 20):
        print("Es invierno")
    elif (current_month == 9 and current_day >= 21) or current_month == 10 or current_month == 11 or (current_month == 12 and current_day <= 20):
        print("Es primavera")
    elif (current_month == 12 and current_day >= 21) or current_month == 1 or current_month == 2 or (current_month == 3 and current_day <= 20):
        print("Es verano")
    elif (current_month == 3 and current_day >= 21) or current_month == 4 or current_month == 5 or (current_month == 6 and current_day <= 20):
        print("Es otoño")

else:
    print("Hemisferio no válido.")
