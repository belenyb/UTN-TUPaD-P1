# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
user_number = int(input("Ingrese un número entero: "))
user_number_str = str(user_number)
total_digits = 0

for index in range(len(user_number_str)):
    # Si el número es negativo, se saltea la iteración del primer ciclo (digit == 0) para no contar el signo
    # negativo como dígito
    if user_number < 0 and index == 0:
        continue
    total_digits += 1
print(f"El número {user_number} tiene {total_digits} dígitos:")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
user_min_number = int(input("Ingrese un número de inicio: "))
user_max_number = int(input("Ingrese un número de finalización: "))
total_sum = 0

# Se suma +1 al valor de inicio para excluirlo de la suma
for number in range(user_min_number + 1, user_max_number):
    total_sum += number
print(total_sum)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
total_sum = 0
not_zero = True
print("Ingrese números enteros para sumar (ingrese 0 para detener): ")

while not_zero:
    user_input = int(input("Ingrese un número entero: "))
    # Usamos la bandera booleana not_zero para manejar cuando salir del bucle
    if user_input == 0:
        not_zero = False
    else:
        total_sum += user_input
        print(f"Número ingresado: {user_input}, Suma parcial: {total_sum}")

print(f"Total acumulado: {total_sum}")
print("Programa finalizado.")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

random_number = random.randint(0, 9)
total_attempts = 0
isPlaying = True

while isPlaying:
    user_input = int(input("Adivine un número del 0 al 9: "))
    if user_input == random_number:
        isPlaying = False
        print("Ganaste! :)")
    total_attempts += 1
print(f"Necesitaste {total_attempts} intentos para adivinar el número.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for digit in range(100, -1, -2):
    print(digit)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
user_positive_num = int(input("Ingrese un número entero positivo: "))
total_sum = 0

if user_positive_num > 0:
    for number in range(user_positive_num + 1):
        total_sum += number
print(f"La suma total de todos los números comprendidos entre 0 y {user_positive_num} es: {total_sum}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
total_positives = 0
total_negatives = 0
total_odds = 0
total_evens = 0

for number in range(100):
    user_number = int(input("Ingrese un número entero: "))

    if user_number > 0:
        total_positives += 1
    else:
        total_negatives += 1

    if user_number % 2 == 0:
        total_evens += 1
    else:
        total_odds += 1

print(f'''Del total de números ingresados:
        > {total_positives} son positivos
        > {total_negatives} son negativos
        > {total_evens} son pares
        > {total_odds} son impares
    ''')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
total_sum = 0
max_range_value = 100

for index in range(max_range_value):
    user_number = int(input("Ingrese un número entero: "))
    total_sum += user_number

mean = total_sum / max_range_value
print(f"La media de los números ingresados es: {mean}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
user_input = input("Ingrese un número: ")
inverted_user_input = user_input[::-1]  # Slicing para invertir el string
print(f"El número invertido es: {inverted_user_input}")
