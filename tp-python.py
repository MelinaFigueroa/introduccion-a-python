# Función para calcular el promedio de notas
def calcular_promedio():
    notas = []
    print("Ingresa las notas (escribi '0' para terminar):")
    while True:
        try:
            nota = float(input("Nota: "))
            if nota == 0:
                break
            notas.append(nota)
        except ValueError:
            print("\nPor favor, ingresa un número válido.\n")
    if len(notas) == 0:
        return "No se ingresaron notas."
    promedio = round(sum(notas) / len(notas), 2)  # Redondear a 2 decimales
    return promedio


# Función para determinar si un color es primario
def es_color_primario():
    color = input("\nIngresa un color: ").strip()
    colores_primarios = ['rojo', 'amarillo', 'azul']
    if color.lower() in colores_primarios:
        print(f"\nEl color {color} es primario.")
    else:
        print(f"\nEl color {color} no es primario.")

# Función para encontrar el número mayor en una serie de números
def numero_mayor():
    numeros = []
    print("\nIngresa los números (escribi '0' para terminar):\n")
    while True:
        try:
            numero = float(input("Número: "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            print("\nPor favor, ingresa un número válido.\n")
    if len(numeros) == 0:
        return "No se ingresaron números."
    mayor = max(numeros)
    return int(mayor) if mayor.is_integer() else mayor


# Función para dibujar un rectángulo de X filas y X columnas
def dibujar_rectangulo():
    try:
        filas = int(input("\nIngresa el número de filas: "))
        columnas = int(input("\nIngresa el número de columnas: "))
        for i in range(filas):
            print("*" * columnas)
    except ValueError:
        print("\nPor favor, ingresa valores enteros para las filas y columnas.\n")

# Función para calcular el factorial de un número entero positivo
def calcular_factorial():
    try:
        numero = int(input("\nIngresa un número entero positivo: "))
        if numero < 0:
            return "\nEl número debe ser positivo."
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial
    except ValueError:
        return "\nPor favor, ingresa un número entero válido.\n"

# Menú para probar las funciones
def menu():
    while True:
        print("\nSelecciona una opción:\n")
        print("1. Calcular promedio de notas")
        print("2. Determinar si un color es primario")
        print("3. Encontrar el número mayor")
        print("4. Dibujar un rectángulo")
        print("5. Calcular factorial")
        print("6. Salir")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            print("\nEl promedio de notas es:", calcular_promedio())
        elif opcion == "2":
            es_color_primario()
        elif opcion == "3":
            print("\nEl número mayor es:", numero_mayor())
        elif opcion == "4":
            dibujar_rectangulo()
        elif opcion == "5":
            print("\nFactorial:", calcular_factorial())
        elif opcion == "6":
            print("\n¡Hasta pronto!")
            break
        else:
            print("\nPor favor, elegí una opción válida.\n")

# Ejecutar el menú
menu()
