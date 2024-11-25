import leer_imprimir_matriz as lim
import jacobi as jc
from misc import limpiar_terminal, imprime_titulo_4

def valida_confirmacion():
    confirmacion = None
    
    while True:
        confirmacion = input("Confirme su elección (S/N): ").strip().upper()
        if confirmacion == "S" or confirmacion == "N":
            break
        else:
            print("\nOpcion invalida, vuelva a intentar.")
    
    return confirmacion


def menu_solucion_matrices():
    opc = 0
    confirmacion = "N"
    
    # Definicion del numero de opcion para cada tarea
    leer_matriz = 1
    imprimir_matriz = 2
    solucion_matriz = 3
    salida = 4

    # Variables ocupadas para los calculos
    matriz = None
    determinante = 0
    n = 0
    dominante = True
    vector = None
    simetria = False
    
    while opc != salida:
        limpiar_terminal()
        titulo = "MENÚ DE SOLUCIÓN DE SISTEMAS DE ECUACIONES LINEALES"
        print("\u2554" + (len(titulo) + 4) * "\u2550" + "\u2557")
        print("\u2551  " + titulo + "  \u2551")
        print("\u255A" + (len(titulo) + 4) * "\u2550" + "\u255D\n")
        
        print("1) Leer matriz y vector.")
        print("2) Imprimir matriz y vector.")
        if determinante != 0:
            print("3) Solución del sistema por el método de Jacobi.")
        print("4) Regresar al menú principal.\n")
        
        opc = int(input("Ingrese una opción: "))
        
        if opc == leer_matriz:
            print("\nSeleccionaste: Leer matriz y vector.")
            
            confirmacion = valida_confirmacion()
            
            if confirmacion == "S":
                limpiar_terminal()
                imprime_titulo_4("LECTURA DE MATRIZ Y VECTOR INDEPENDIENTE")
                
                matriz, n = lim.leer_matriz()
                dominante, determinante, simetria = lim.det_dom_simetria(matriz, n)

                print("\n") # Deja dos espacios entre la lectura de la matriz y del vector.
                vector = lim.leer_vector(n)
                
                print("\n\n\u25CF Se ha leído la matriz y el vector satisfactoriamente.\n")
                input("Presione enter para regresar al menú de solución de sistemas.")
                
        elif opc == imprimir_matriz:
            print("\nSeleccionaste: Imprimir matriz y vector")
            confirmacion = valida_confirmacion()
            
            if confirmacion == "S":
                if matriz is None:
                    print("\n¡Pero no has dado ninguna matriz!")
                else:
                    print("\n\u27a5 Matriz:")
                    print(matriz)
                    print("\n\u27a5 Vector:")
                    print(vector)
                input("\nPresione enter para ingresar otra opción.")
                
        elif opc == solucion_matriz:
            if determinante != 0:
                limpiar_terminal()
                imprime_titulo_4("SOLUCIÓN DEL SISTEMA POR EL MÉTODO DE JACOBI")
                jc.opciones(matriz, vector, n, dominante)
                
        elif opc == salida:
            input("Presione enter para regresar al menú principal.")
        else:
            print("\nOpción incorrecta :(")
            input("Presione enter para ingresar otra opción.")