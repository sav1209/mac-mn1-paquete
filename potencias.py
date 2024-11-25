import numpy as np
from misc import limpiar_terminal, imprime_titulo_3, imprime_titulo_4
import leer_imprimir_matriz as lim


# Lee los datos necesarios para aplicar el método de potencias
def lectura_datos():
    limpiar_terminal()
    imprime_titulo_3("OBTENCION DE VALORES PROPIOS - LECTURA DE DATOS")
    matriz, n = lim.leer_matriz()

    # Valida que la norma espectral del vector inicial sea de 1
    norma = None
    while True:
        limpiar_terminal()
        imprime_titulo_3("OBTENCION DE VALORES PROPIOS - LECTURA DE DATOS")
        vi = lim.leer_vector(n)  # Vector columna inicial
        norma = max(abs(vi))
        if norma == 1:
            break
        else:
            print("La norma espectral del vector inicial debe ser 1. Vuelva a ingresar.")
            input("\nPresione enter para continuar.")

    limpiar_terminal()
    imprime_titulo_3("OBTENCION DE VALORES PROPIOS - LECTURA DE DATOS")

    # Leer tolerancia y número máximo de iteraciones
    print("\u25E2 LECTURA DE LA TOLERANCIA Y MÁXIMO DE ITERACIONES \u25E3\n")
    tolerancia = float(input("Introduce la tolerancia para el criterio de paro: "))
    max_iter = int(input("Introduce el número máximo de iteraciones: "))

    return n, matriz, vi, max_iter, tolerancia


# Aplica el método de potencias con una matriz A de n*n y vector inicial x
def metodo_potencias(A, x, tolerancia, max_iter):
    # Inicialización
    lambda_anterior = 0

    print("\t\u25A0 SUCESIÓN DE VECTORES \u25A0\n")
    # Iteración principal
    for iteracion in range(1, max_iter + 1):
        # Producto matriz-vector: y = A * x
        y = np.dot(A, x)

        # Calcula la magnitud máxima
        magnitud_maxima = np.max(np.abs(y))

        # Filtra los valores con la magnitud máxima
        valores_maximos = y[np.abs(y) == magnitud_maxima]

        # Selecciona el valor positivo si existe, o tomar el único disponible
        lambda_actual = np.max(valores_maximos)

        # Normalizar el vector: x = y / lambda_actual
        x = y / lambda_actual

        error = abs(abs(lambda_actual) - abs(lambda_anterior))
        print("\u25CF Iteración", iteracion)
        print(f"\u27A4 \u03BB^({iteracion}) = {lambda_actual}") # \u03BB = λ, caracter lambda en Unicode
        print("\u27A4 Error =", error)
        print(f"\u27A4 x^({iteracion}) =")
        print(x, end="\n\n")

        # Verificar criterio de parada
        if error < tolerancia:
            print("\n\t\u25A0 SOLUCIÓN \u25A0")
            print(f"\u25B7 Convergencia alcanzada en {iteracion} iteraciones.")
            print(f"\u25B7 Valor propio dominante: {lambda_actual}")
            print("\u25B7 Vector propio asociado:")
            print(x)
            return lambda_actual, x # Salir del programa al converger

        # Actualizar para la siguiente iteración
        lambda_anterior = lambda_actual

    # Si no converge
    print("\n\t\u25A0 SOLUCIÓN \u25A0")
    print(f"\u25B7 El método no convergió en {max_iter} iteraciones.")
    print(f"\u25B7 Último valor aproximado del valor propio dominante: {lambda_actual}")
    print("\u25B7 Último vector propio asociado:")
    print(x)
    return lambda_actual, x


# Aplica el método de potencias inverso con una matriz A y vector inicial x
def metodo_potencias_inverso(A, x, tolerancia, max_iter):
    # Inicialización
    lambda_anterior = 1

    print("\t\u25A0 SUCESIÓN DE VECTORES \u25A0\n")
    # Iteración principal
    for iteracion in range(1, max_iter + 1):
        # Producto matriz-vector: y = A * x
        y = np.dot(A, x)

        # Calcula la magnitud máxima
        magnitud_maxima = np.max(np.abs(y))

        # Filtra los valores con la magnitud máxima
        valores_maximos = y[np.abs(y) == magnitud_maxima]

        # Selecciona el valor positivo si existe, o tomar el único disponible
        lambda_actual = np.max(valores_maximos)

        # Normalizar el vector: x = y / lambda_actual
        x = y / lambda_actual

        error = abs(abs(lambda_actual) - abs(lambda_anterior))
        print("\u25CF Iteración", iteracion)
        print(f"\u27A4 \u03BB^({iteracion}) = {1 / lambda_actual}") # \u03BB = λ, caracter lambda en Unicode
        print("\u27A4 Error = ", error)
        print(f"\u27A4 x^({iteracion}) =")
        print(x, end="\n\n")

        # Verificar criterio de parada
        if error < tolerancia:
            print("\n\t\u25A0 SOLUCIÓN \u25A0")
            print(f"\u25B7 Convergencia alcanzada en {iteracion} iteraciones.")
            print(f"\u25B7 Valor propio dominante: {1 / lambda_actual}")
            print(f"\u25B7 Vector propio asociado:")
            print(x)
            return 1 / lambda_actual, x # Salir del programa al converger

        # Actualizar para la siguiente iteración
        lambda_anterior = lambda_actual

    # Si no converge
    print("\n\t\u25A0 SOLUCIÓN \u25A0")
    print(f"\u25B7 El método no convergió en {max_iter} iteraciones.")
    print(f"\u25B7 Último valor aproximado del valor propio dominante: {1 / lambda_actual}")
    print(f"\u25B7 Último vector propio asociado:")
    print(x)
    return 1 / lambda_actual, x


# Aplica ambos métodos a una matriz A con vector inicial x
def potencias_y_potencias_inverso(A, x, tolerancia, max_iter):
    limpiar_terminal()
    imprime_titulo_3("OBTENCION DE VALORES PROPIOS - RESULTADOS")
    print("Datos ingresados:")
    print("\u25C8 Matriz:")
    print(A)
    print("\u25C8 Vector inicial:")
    print(x)
    print(f"\u25C8 Tolerancia: {tolerancia}")
    print(f"\u25C8 Número máximo de iteraciones: {max_iter}\n")

    imprime_titulo_4("Valor y vector propio máximo")
    valor_propio_max, vector_propio_max = metodo_potencias(A, x, tolerancia, max_iter)

    print("\n")

    imprime_titulo_4("Valor y vector propio mínimo")
    try:
        invA = np.linalg.inv(A)
        valor_propio_min, vector_propio_min = metodo_potencias_inverso(invA, x, tolerancia, max_iter)
        print("\n")
    except np.linalg.LinAlgError:
        print("La matriz ingresada es singular, por lo que no tienen inversa y no se puede aplicar el método de potencias inverso.")
        print("Pero en este caso el valor propio 0 y el vector asociado es cualquier x tal que al multiplicarlo por la matriz de la matriz 0.\n")
        valor_propio_min, vector_propio_min = 0, "No se pudo determinar"

    imprime_titulo_4("Resumen")
    print(f"\u25B7 Valor propio máximo: {valor_propio_max}")
    print("\u25B7 Vector asociado:")
    print(vector_propio_max)

    print(f"\n\u25B7 Valor propio mínimo: {valor_propio_min}")
    print(f"\u25B7 Vector asociado:")
    print(vector_propio_min)

    input("\nPresiona enter para regresar al menu principal")