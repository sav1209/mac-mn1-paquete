import numpy as np


def seleccionar(opcion, vect_inic, iteraciones, tolerancia):
    if opcion == 1:
        x = int(input("¿Que elemento vas a modificar?: "))
        vect_inic[x-1] = float(input("Ingresa el nuevo valor: "))
    elif opcion == 2:
        iteraciones = int(input("Ingresa el nuevo límite de iteraciones: "))
    elif opcion == 3:
        tolerancia = float(input("Ingresa la nueva tolerancia: "))
    else:
        print("Opción incorrecta")
    return vect_inic, iteraciones, tolerancia


def opciones(matriz, vector, n, es_edd):
    if not es_edd:
        print("\nLa convergencia no se garantiza por no tratarse de un sistema EDD")
    
    tolerancia = float(input("\u27A4 Ingrese la tolerancia de error: "))
    iteraciones = int(input("\u27A4 Ingrese el número máximo de iteraciones: "))
    
    vect_inic = np.zeros([n, 1])
    print("\u27A4 Ingrese los coeficientes del vector inicial:")
    for i in range(n):
        vect_inic[i] = float(input(f"\t\u27A4 x_({i+1}): "))
    
    while True:
        print("\n\u25C9 El vector inicial es:")
        print(vect_inic)
        print(f"\u25C9 El número máximo de iteraciones es: {iteraciones}")
        print(f"\u25C9 La tolerancia es: {tolerancia}")
        es_correcto = input("\n¿Es correcto el ingreso de datos? (s/n): ").upper()
        if es_correcto == "S":
            break
        else:
            opcion = int(input("¿Qué desea modificar?\n1. Vector inicial\n2. Límite de iteraciones\n3. Tolerancia\n"))
            vect_inic, iteraciones, tolerancia = seleccionar(opcion, vect_inic, iteraciones, tolerancia)
    
    jacobi(matriz, vector, vect_inic, tolerancia, iteraciones, n)


def jacobi(matriz, vector, x0, tol, max_iter, n):
    # Matrices en forma matricial del método iterativo de Jacobi
    # x = Tx + C
    T = np.zeros([n, n])
    C = np.zeros([n, 1])

    # Calcula las entradas de T y C
    for i in range(n):
        for j in range(n):
            T[i][j] = - matriz[i][j] / matriz[i][i]
        T[i][i] = 0
        C[i] = vector[i] / matriz[i][i]

    k = 0 # Numero de iteracion
    print("\n\n\t\u25A0 SUCESIÓN DE VECTORES \u25A0\n")
    print("\u25CF Iteración 0")
    print("\u27A4 x^0 = ")
    print(x0, end="\n\n")
    while k < max_iter:
        k += 1
        xk = np.matmul(T, x0) + C
        error = np.linalg.norm(xk - x0, np.inf)
        x0 = xk
        
        print("\u25CF Iteración", k)
        print("\u27A4 Error: ", error)
        print(f"\u27A4 x^({k}) =")
        print(xk, end="\n\n")

        if error < tol:
            break

    print("\n\t\u25A0 SOLUCIÓN \u25A0")
    print(f"\u27A4 La solución con una tolerancia de {tol} y un máximo de {max_iter} iteraciones es:")
    print(xk)
    
    input("\n\nPresione enter para regresar al menú principal.")