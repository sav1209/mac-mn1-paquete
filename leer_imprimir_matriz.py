import numpy as np


# Calcula el determinante de 'matriz' de 'n' * 'n' utilizando triangulación.
def determinante_triangulacion(matriz, n):
    det = 1
    matriz_triangular = matriz.copy()

    for col in range(n):
        if matriz_triangular[col][col] == 0:
            return 0
        else:
            det *= matriz_triangular[col][col]
            for fila in range(col + 1, n):
                factor = matriz_triangular[fila][col] / matriz_triangular[col][col]
                for i in range(col, n):
                    matriz_triangular[fila][i] -= factor * matriz_triangular[col][i]

    return det


# Determina si 'matriz' de 'n'*'n' es simetrica
def es_simetrica(matriz, n):
    for i in range(n):
        for j in range(i):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


# Determina si 'matriz' 'n'*'n' es dominante
def es_dominante(matriz, n):
    for i in range(n):
        suma = 0
        for j in range(n):
            if i != j:
                suma += abs(matriz[i][j])
        if abs(matriz[i][i]) < suma:
            return False
    return True


def det_dom_simetria(matriz, n):
    dominante = es_dominante(matriz, n)  # Determina si la matriz es EDD
    if dominante:
        determinante = 1  # Se usa un valor aleatorio diferente de cero pues este dato no se ocupará después.
        print("\n\u25B6 La matriz ingresada es dominante diagonalmente.")
    else:
        determinante = determinante_triangulacion(matriz, n)
        if determinante != 0:
            print(f"\n\u25B6 El determinante es {determinante}, por tanto NO se garantiza la convergencia.")
        else:
            print(
                "\n\u25B6 Un sistema con la matriz ingresada NO tiene solución o se generó una división por cero al calcular el determinante por triangulación.")

    simetrica = es_simetrica(matriz, n)
    return dominante, determinante, simetrica

# Lee una matriz
def leer_matriz():
    # Solicita y valida la dimensión de la matriz

    print("\u25E2 LECTURA DE LA MATRIZ \u25E3\n")
    
    n = int(input("Dame la dimensión de la matriz: "))
    while True:
        correcto = input(f"¿Es {n} la dimensión correcta? (S/N): ").strip().upper()
        if correcto == "S":
            break
        elif correcto == "N":
            print("Dimensión incorrecta")
            n = int(input("Dame la dimensión de la matriz: "))
        else:
            print("Opción incorrecta :(")

    # Lectura de la matriz
    matriz = np.zeros((n, n))
    print("\nIngrese los valores de la matriz:")
    for i in range(n):
        for j in range(n):
            matriz[i][j] = float(input(f"\t\u27A4 Posición ({i+1},{j+1}): "))
        
    print("\nLa matriz ingresada es:")
    print(matriz)
    
    # Corrección del algún coeficiente
    correccion = input("\n¿Desea corregir algún coeficiente (S/N)? ").strip().upper()
    while True:
        if correccion == "S":
            print("\n\u25A0 Corrigiendo un coeficiente")
            while True:
                print("\u25cf Ingrese los datos del coeficiente a corregir.")
                i = int(input("  \u2726 Renglón: ")) - 1
                j = int(input("  \u2726 Columna: ")) - 1
                if 0 <= i < n and 0 <= j < n:
                    matriz[i][j] = float(input("\u25cf Ingrese el nuevo coeficiente: "))
                    print("\nDespués de la última corrección se obtiene lo siguiente:")
                    print(matriz)
                    break
                else:
                    print(f"Los indices deben estar entre 1 y {n} (incluyendolos). Vuelva a intentar.")
        elif correccion == "N":
            break
        else:
            print("Opcion invalida, vuelva a intentar.")
        
        correccion = input("\n¿Desea corregir otro coeficiente (S/N)? ").upper()

    return matriz, n


# Lee un vector columna
def leer_vector(n):
    print("\u25E2 LECTURA DEL VECTOR INDEPENDIENTE \u25E3\n")
    
    vector = np.zeros((n, 1))

    print("Ingrese los valores del vector independiente en la posición dada: ")
    for i in range(n):
        vector[i] = float(input(f"\t\u27A4 Posición {i+1}: "))

    print("\nEl vector ingresado es:")
    print(vector)
    
    # Corrección del algún coeficiente
    correccion = input("\n¿Desea corregir algún coeficiente (S/N)? ").strip().upper()
    while True:
        if correccion == "S":
            print("\n\u25A0 Corrigiendo un coeficiente")
            while True:
                i = int(input("\u25cf Ingrese la posición del coeficiente a corregir: ")) - 1
                if 0 <= i < n:
                    vector[i] = float(input("\u25cf Ingrese el nuevo coeficiente: "))
                    print("\nDespués de la última corrección se obtiene lo siguiente:")
                    print(vector)
                    break
                else:
                    print(f"La posición debe estar entre 1 y {n} (incluyendolos). Vuelva a intentar.")
        elif correccion == "N":
            break
        else:
            print("Opcion invalida, vuelva a intentar.")

        correccion = input("\n¿Desea corregir otro coeficiente (S/N)? ").strip().upper()
    
    return vector