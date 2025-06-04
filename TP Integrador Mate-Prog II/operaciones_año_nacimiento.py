from datetime import date

### --- Parte 2B: Operaciones con años de nacimiento --- ###

def ingresar_anios_nacimiento():
    """
    Solicita al usuario que ingrese 4 años de nacimiento.

    Returns:
        list: Lista de 4 años como enteros.
    """
    anios = []
    for i in range(4):
        anio = int(input(f"Ingrese el año de nacimiento de la persona {i + 1}: "))
        anios.append(anio)
    return anios

def contar_pares_impares(anios):
    """
    Cuenta cuántos años son pares e impares.

    Args:
        anios (list): Lista de años.

    Returns:
        tuple: Cantidad de pares e impares.
    """
    pares = impares = 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def es_bisiesto(anio):
    """
    Verifica si un año es bisiesto.

    Args:
        anio (int): Año a evaluar.

    Returns:
        bool: True si es bisiesto, False si no.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def edades_actuales(anios):
    """
    Calcula la edad actual de cada persona a partir de su año de nacimiento.

    Args:
        anios (list): Lista de años de nacimiento.

    Returns:
        list: Lista de edades.
    """
    anio_actual = date.today().year
    return [anio_actual - anio for anio in anios]

def producto_cartesiano(anios, edades):
    """
    Calcula el producto cartesiano entre años de nacimiento y edades actuales.

    Args:
        anios (list): Lista de años.
        edades (list): Lista de edades.

    Returns:
        list: Lista de tuplas (año, edad).
    """
    return [(anio, edad) for anio in anios for edad in edades]

# Años de nacimiento por defecto:
anios_defecto = [1993, 1999, 1982, 1988]

# Selección de uso de años por defecto o ingreso manual
selec_anios = input("\n¿Desea usar años de nacimiento por defecto (D) o ingresar nuevos (N)?: ").upper()
while selec_anios != "D" and selec_anios != "N":
    print("Opción incorrecta.")
    selec_anios = input("¿Desea usar años de nacimiento por defecto (D) o ingresar nuevos (N)?: ").upper()

if selec_anios == "N":
    anios = ingresar_anios_nacimiento()
else:
    anios = anios_defecto

# Conteo de pares e impares
pares, impares = contar_pares_impares(anios)
print(f"\nCantidad de años pares: {pares}")
print(f"Cantidad de años impares: {impares}")

# Evaluación lógica: todos después del 2000
if all(anio > 2000 for anio in anios):
    print("Grupo Z: todos nacieron después del 2000.")
else:
    print("El grupo incluye personas nacidas antes del 2000.")

# Evaluación lógica: si hay al menos un año bisiesto
if any(es_bisiesto(anio) for anio in anios):
    print("Tenemos un año especial: al menos un integrante nació en un año bisiesto.")
else:
    print("Ningún integrante nació en un año bisiesto.")

# Producto cartesiano: años x edades
edades = edades_actuales(anios)
producto = producto_cartesiano(anios, edades)
print("\nProducto cartesiano entre años y edades:")
for par in producto:
    print(par)
