from misc import limpiar_terminal, imprime_titulo_3, imprime_titulo_4
from tabulate import tabulate # Creación de tablas.
import numpy as np

# CONSTANTES
# Métodos implementados
metodos = ("Método de Newton", "Método de la secante", "Método de bisección")

# Opciones de funciones a resolver.
funciones = [
    {
        "asciimath": "f(x) = x^2 cos(x) - 2x",
        "func": lambda x: x**2 * np.cos(x) - 2*x,
        "derivada": lambda x: 2 * x * np.cos(x) - x ** 2 * np.sin(x) - 2
    },
    {
        "asciimath": "f(x) = (6 - 2/x^2)(e^(2+x)/4) + 1",
        "func": lambda x: (6 - 2/x**2)*(np.e**(2 + x)/4) + 1,
        "derivada": lambda x: np.e**(2 + x) * (1 / 4 * (6 - 2/x**2) + 1 / x**3)
    },
    {
        "asciimath": "f(x) = x^3 - 3sin(x^2) + 1",
        "func": lambda x: x**3 - 3*np.sin(x**2) + 1,
        "derivada": lambda x: 3 * x ** 2 - 6 * x * np.cos(x ** 2)
    },
    {
        "asciimath": "f(x) = x^3 + 6x^2 + 9.4x + 2.5",
        "func": lambda x: x**3 + 6*x**2 + 9.4*x + 2.5,
        "derivada": lambda x: 3 * x ** 2 + 12 * x + 9.4
    },
]


def newton(x0, f_x0, f_prima_x0):
    if f_prima_x0 == 0 or f_x0 == 0:
        return "err"
    x1 = x0 - f_x0 / f_prima_x0
    return x1


def iteracion_newton(func, x0, max_iter, tol):
    funcion = funciones[func - 1]["func"]
    derivada = funciones[func - 1]["derivada"]
    iter = 0
    error = 100
    fx0 = 0
    fpx0 = 0
    print("i\t\tx_k\t\tf(x_k)\t\tf'(x_k)\t\tE_r")
    while (iter < max_iter and error > tol):
        iter += 1
        fx0 = funcion(x0)
        fpx0 = derivada(x0)
        x1 = newton(x0, fx0, fpx0)
        if x1 == "err":
            print("Se detuvo la iteración, hay una indeterminación con los valores obtenidos")
            return
        error = abs(x1 - x0) / abs(x1)
        print(f"{iter}\t{x0:.6f}\t{fx0:.6f}\t{fpx0:.6f}\t{error:.6f}")
        x0 = x1
    if error > tol:
        print("No se alcanzó la tolerancia")
    print(f"Raíz encontrada: {x0} en la iteración {iter + 1}")


def metodo_secante(f, valores_iniciales, tol, tipo_error, max_iteraciones):
    # Verifica que los argumentos proporcionados sean validos
    ## 'valores_iniciales' debe ser una tupla de dos elementos.
    if not isinstance(valores_iniciales, tuple) or len(valores_iniciales) != 2:
        print("'valores_iniciales' debe ser una tupla de 2 elementos.")
        return

    ## La tolerancia 'tol' debe ser un numero positivo.
    if not isinstance(tol, (int, float)) or tol <= 0:
        print("La tolerancia debe ser un número positivo.")
        return

    ## 'tipo_error' debe ser alguno de los siguiente enteros: 0, 1, 2, 3.
    if not isinstance(tipo_error, int) or tipo_error < 0 or tipo_error > 3:
        print("El tipo de error debe ser 0, 1, 2 o 3.")
        return

    ## max_iteraciones debe ser un numero entero positivo.
    if not isinstance(max_iteraciones, int) or max_iteraciones <= 0:
        print("El máximo de iteraciones debe ser un entero positivo")
        return

    # Inicializa los valores iniciales y evalua la función en estos
    x0 = valores_iniciales[0]
    fx0 = f(x0)
    x1 = valores_iniciales[1]
    fx1 = f(x1)

    # Verifica que si la solución es alguno de los extremos
    if fx0 == 0:
        print(f"{x0} es una raíz de la función.")
        return
    if fx1 == 0:
        print(f"{x1} es una raíz de la función.")
        return

    # Lista para almacenar la tabla del proceso.
    tabla = []
    # Declara un encabezado para la tabla.
    encabezado = ["k", "x_(k-1)", "x_k", "f(x_(k-1))", "f(x_k)", "x_(k+1)", "f(x_(k+1))", "Ea", "Er", "Er%"]

    # Arreglo para almacenar las medidas del error
    errores = []
    tipos_errores = ("absoluto", "relativo", "porcentual")

    # Calcula la abscisa del punto de intersección de la secante con el eje X y la evalúa en la función
    try:
        x = x1 - fx1 * (x0 - x1) / (fx0 - fx1)
        fx = f(x)
    except ZeroDivisionError:
        print("ERROR: División por cero detectada. Revisa los valores ingresados.")
        return

    # Calculo de las medidas del error.
    ## Error absoluto
    errores.append(abs(x1 - x0))
    ## Error relativo y porcentual
    if x1 != 0:
        errores.append(errores[-1]/abs(x1))
        errores.append(errores[-1] * 100)
    else:
        errores.append("ERROR")
        errores.append("ERROR")

    tabla.append([1, x0, x1, fx0, fx1, x, fx, errores[0], errores[1], errores[2]])

    for i in range(2,max_iteraciones+1):
        x0 = x1
        x1 = x
        fx0 = f(x0)
        fx1 = f(x1)

        try:
            x = x1 - fx1*(x0 - x1)/(fx0 - fx1)
            fx = f(x)
        except:
            input("ERROR: División por cero detectada. Presione enter para mostrar los resultados hasta este error.")
            break

        # Calculo de las medidas del error.
        errores.clear()
        ## Error absoluto
        errores.append(abs(x1 - x0))
        ## Error relativo y porcentual
        if x1 != 0:
            errores.append(errores[-1]/abs(x1))
            errores.append(errores[-1] * 100)
        else:
            errores.append("ERROR")
            errores.append("ERROR")

        tabla.append([i, x0, x1, fx0, fx1, x, fx, errores[0], errores[1], errores[2]])

        # Comprueba si se alcanzo la condicion de paro.
        if tipo_error != 3 and errores[tipo_error] != "ERROR" and errores[tipo_error] < tol or fx1 == 0:
            break

    # Imprime la tabla
    print(tabulate(tabla, headers=encabezado, tablefmt="fancy_grid", floatfmt=".10f"))

    # Imprime resultados
    if isinstance(errores[tipo_error], str) or (tipo_error != 3 and errores[tipo_error] >= tol):
        print("\n¡EL METODO FALLO HASTA LA ÚLTIMA ITERACIÓN!")
        print(f"La mejor aproximación a la raíz fue {x} con un error {tipos_errores[tipo_error]} de {errores[tipo_error]}")
    else:
        print(f"\nRaíz obtenida: {x1}")
        print(f"La raíz se obtuvo en la iteración {i} con un error {tipos_errores[tipo_error]} de {errores[tipo_error]}")


def metodo_biseccion(f, intervalo_inicial, tol, tipo_error, max_iteraciones):
    # Verifica que los argumentos proporcionados sean validos
    ## 'valores_iniciales' debe ser una tupla de dos elementos y el primer elemento debe ser menor al segundo.
    if not isinstance(intervalo_inicial, tuple) or len(intervalo_inicial) != 2:
        print("'intervalo_inicial' debe ser una tupla de 2 elementos.")
        return
    elif intervalo_inicial[0] > intervalo_inicial[1]:
        print("El intervalo inicial es invalido.")
        return

    ## La tolerancia 'tol' debe ser un numero positivo.
    if not isinstance(tol, (int, float)) or tol <= 0:
        print("La tolerancia debe ser un número positivo.")
        return

    ## 'tipo_error' debe ser alguno de los siguiente enteros: 0, 1, 2, 3.
    if not isinstance(tipo_error, int) or tipo_error < 0 or tipo_error > 3:
        print("El tipo de error debe ser 0, 1, 2 o 3.")
        return

    ## max_iteraciones debe ser un numero entero positivo.
    if not isinstance(max_iteraciones, int) or max_iteraciones <= 0:
        print("El máximo de iteraciones debe ser un entero positivo")
        return


    # Inicializa los extremos del intervalo proporcionado y evalua la funcion en estos.
    a = intervalo_inicial[0]
    b = intervalo_inicial[1]
    fa = f(a)
    fb = f(b)

    # Debe existir un cambio de signo para que haya una raiz en intervalo proporcionado.
    if fa * fb > 0:
        print("ES POSIBLE QUE NO EXISTA UNA RAÍZ EN EL INTERVALO INICIAL")
        return
    elif fa == 0:
        print(f"{a} es una raíz de la función.")
        return
    elif fb == 0:
        print(f"{b} es una raíz de la función.")
        return

    # Lista para almacenar la tabla del proceso.
    tabla = []

    # Obtiene el punto medio de [a,b] y evalua la funcion en este.
    p = (a + b)/2
    fp = f(p)

    # Declara un encabezado para la tabla y añade la primer fila
    encabezado = ["k", "a_k", "b_k", "f(a_k)", "f(b_k)", "p_k", "f(p_k)", "Ea", "Er", "Er%"]
    tabla.append([0, a, b, fa, fb, p, fp])


    # En caso de que la solución maravillosamente se encuentre en la primer iteración.
    if fp == 0:
        print(tabulate(tabla, headers=encabezado, tablefmt="fancy_grid", floatfmt=".10f"),"\n")
        print(f"Raíz obtenida: {p}")
        print(f"La raíz exacta se obtuvo en la iteración 0.")
        return


    # Reasigna el intervalo según donde se encuentre el cambio de signo.
    if fa * fp < 0:
        b = p
        fb = f(b)
    else:
        a = p
        fa = f(a)

    errores = []
    tipos_errores = ("absoluto", "relativo", "porcentual")
    for i in range(1,max_iteraciones):
        p_anterior = p
        p = (a + b)/2
        fp = f(p)

        # Calculo de las medidas del error.
        errores.clear()
        ## Error absoluto
        errores.append(abs(p - p_anterior))
        ## Error relativo y porcentual
        if p != 0:
            errores.append(errores[-1]/abs(p))
            errores.append(errores[-1] * 100)
        else:
            errores.append("ERROR")
            errores.append("ERROR")

        tabla.append([i, a, b, fa, fb, p, fp, errores[0], errores[1], errores[2]])

        # Comprueba si se alcanzo la condicion de paro.
        if tipo_error != 3 and errores[tipo_error] != "ERROR" and errores[tipo_error] < tol or fp == 0:
            break
        elif fa * fp < 0:
            b = p
            fb = f(b)
        else:
            a = p
            fa = f(a)

    # Imprime la tabla
    print(tabulate(tabla, headers=encabezado, tablefmt="fancy_grid", floatfmt=".10f"))

    # Imprime resultados
    if len(errores) == 0:
        print(f"\nLa mejor aproximación a la raíz fue {p} pero no se puede determinar el error con una sola iteracion.")
    elif tipo_error != 3 and errores[tipo_error] >= tol:
        print("\n¡EL MÉTODO FALLO HASTA LA ÚLTIMA ITERACIÓN!")
        print(f"La mejor aproximación a la raíz fue {p} con un error {tipos_errores[tipo_error]} de {errores[tipo_error]}")
    else:
        print(f"\nRaíz obtenida: {p}")
        print(f"La raíz se obtuvo en la iteración {i} con un error {tipos_errores[tipo_error]} de {errores[tipo_error]}")


# Menu con los métodos
def menu_metodos():
    opcion = None
    while True:
        limpiar_terminal()
        imprime_titulo_3("MENÚ DE MÉTODOS")
        for indice, metodo in enumerate(metodos):
            print(f"{indice+1}. {metodo}")
        print(f"{indice+2}. Regresar al menu principal.")

        while True:
            opcion = int(input("\n\u25B6 Ingrese una opción: "))
            if opcion < 1 or opcion > (len(metodos) + 1):
                print("Opcion invalida. Vuelva a intentar")
            else:
                break

        print(f"\nLa opción seleccionada fue: {metodos[opcion-1] if 1 <= opcion <= len(metodos) else 'Regresar al menu principal'}.")
        confirma_eleccion = input("\u25B6 ¿Está seguro de su elección? (s/n): ").strip().lower()

        if confirma_eleccion == "s":
            input("\nLa elección ha sido confirmado. Presione enter para continuar.")
            break
        else:
            input("\nVuelva a elegir una opción. Presione enter para continuar.")

    return opcion


# Menu con las funciones.
def menu_funciones():
    opcion = None
    while True:
        limpiar_terminal()
        imprime_titulo_4("MENÚ DE FUNCIONES")
        for indice, funcion in enumerate(funciones):
            print(f"{indice+1}. {funcion['asciimath']}")
        print(f"{indice+2}. Regresar al menú de métodos.")

        while True:
            opcion = int(input("\n\u25B6 Ingrese una opción: "))
            if opcion < 1 or opcion > (len(funciones) + 1):
                print("Opcion invalida. Vuelva a intentar")
            else:
                break

        print(f"La opción seleccionada fue: {funciones[opcion-1]['asciimath'] if 1 <= opcion <= len(funciones) else 'Regresar al menú de métodos.'}")
        confirma_eleccion = input("\u25B6 ¿Está seguro de su elección? (s/n): ").strip().lower()

        if confirma_eleccion == "s":
            input("\nLa elección ha sido confirmado. Presione enter para continuar.")
            break
        else:
            input("\nVuelva a elegir una opción. Presione enter para continuar.")

    return opcion

def principal():
    limpiar_terminal()
    while True:
        opcion_metodo = menu_metodos()
        if opcion_metodo == (len(metodos) + 1):
            break

        while True:
            opcion_funcion = menu_funciones()
            if opcion_funcion == (len(funciones) + 1):
                break

            funcion = funciones[opcion_funcion - 1]
            while True:
                limpiar_terminal()
                print(f"Método: {metodos[opcion_metodo - 1]}")
                print(f"Función: {funcion['asciimath']}")

                print(f"\nIngrese los datos necesarios para el método y función seleccionados:")
                if opcion_metodo == 1: # Método de Newton
                    n1 = float(input("\u25B6 Valor a evaluar: "))
                    tolerancia = float(input("\u25B6 Tolerancia: "))
                    iteraciones = int(input("\u25B6 Máximo de iteraciones: "))
                    iteracion_newton(opcion_funcion, n1, iteraciones, tolerancia)
                elif opcion_metodo == 2: # Método de la secante
                    print("\u25B6 Valores iniciales:")
                    x0 = float(input("\t\u25CF x_0 = "))
                    x1 = float(input("\t\u25CF x_1 = "))
                    tolerancia = float(input("\u25B6 Tolerancia sobre el error relativo: "))
                    iteraciones = int(input("\u25B6 Máximo de iteraciones: "))
                    print() # Deja una linea en blanco
                    metodo_secante(funcion["func"], (x0, x1), tolerancia, 1, iteraciones)
                elif opcion_metodo == 3: # Método de biseccion
                    print("\u25B6 Intervalo inicial [a,b]:")
                    a = float(input("\t\u25CF a = "))
                    b = float(input("\t\u25CF b = "))
                    tolerancia = float(input("\u25B6 Tolerancia sobre el error relativo: "))
                    iteraciones = int(input("\u25B6 Máximo de iteraciones: "))
                    print() # Deja una linea en blanco
                    metodo_biseccion(funcion["func"], (a,b), tolerancia, 1, iteraciones)

                otra_raiz = input("\n\n\u25B6 ¿Desea obtener otra raíz de esta función? (s/n): ").strip().lower()
                if otra_raiz != "s":
                    break