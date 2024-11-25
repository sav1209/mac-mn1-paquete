import menu_metodos_solucion_ec_lin as sel
import metodos_interpolacion as mi
import potencias as pot
from misc import limpiar_terminal, imprime_titulo_2, imprime_titulo_1

def mensaje_inicio():
    imprime_titulo_1("PAQUETE DE PROGRAMAS")
    
    print("\n\t\t\t¡BIENVENIDO!\n")
    print("\u2bc8 ASIGNATURA: Metodos Numericos I")
    print("\u2bc8 INTEGRANTES:")
    print("\t\u2b25 Martínez Rosales Itzel Selene")
    print("\t\u2b25 Ruiz Sánchez Emiliano")
    print("\t\u2b25 Villeda López Saúl\n\n")

    input("Presione enter para ir al menu principal...")


def menu_principal():
    interpolacion = 1
    solucion_sistema = 2
    valores_propios = 3
    salida = 4

    seleccion = 0
    while seleccion != salida:
        limpiar_terminal()
        imprime_titulo_2("MENU PRINCIPAL")
        
        print("1) Solución de ecuaciones.")
        print("2) Solución de sistemas de ecuaciones lineales.")
        print("3) Obtención de valores propios.")
        print("4) Salir.\n")
        
        seleccion = int(input("Escoge una opción: "))
        if seleccion == interpolacion:
            mi.principal()
        elif seleccion == solucion_sistema:
            sel.menu_solucion_matrices()
        elif seleccion == valores_propios:
            n, matriz, vi, max_iter, tolerancia = pot.lectura_datos()
            pot.potencias_y_potencias_inverso(matriz, vi, tolerancia, max_iter)
        elif seleccion == salida:
            print("\nSaliendo del programa...")
        else:
            print("\nOpción incorrecta :(")
            input("\nPresione enter para ingresar otra opción.")


mensaje_inicio()
menu_principal()