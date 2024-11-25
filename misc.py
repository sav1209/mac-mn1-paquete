import os

# Limpia la terminal segun el SO que se este utilizando.
def limpiar_terminal():
    sistema = os.name  # Detecta el sistema operativo
    if sistema == 'posix':  # Linux, macOS
        os.system('clear')
    elif sistema == 'nt':  # Windows
        os.system('cls')


def imprime_titulo_1(titulo):
    titulo = "PAQUETE DE PROGRAMAS"
    decoracion = "\u2588" * (len(titulo) + 12)

    print(decoracion)
    print(4 * "\u2588" + "  " + titulo + "  " + 4 * "\u2588")
    print(decoracion)


def imprime_titulo_2(titulo):
    print("\u259b" + (len(titulo) + 4) * "\u2580" + "\u259c")
    print("\u258c  " + titulo + "  \u2590")
    print("\u2599" + (len(titulo) + 4) * "\u2584" + "\u259f\n")


def imprime_titulo_3(titulo):
    print("\u2554" + (len(titulo) + 4) * "\u2550" + "\u2557")
    print("\u2551  " + titulo + "  \u2551")
    print("\u255A" + (len(titulo) + 4) * "\u2550" + "\u255D\n")


def imprime_titulo_4(titulo):
    print("\u256D" + "\u2500" * (len(titulo) + 2) + "\u256E")
    print("\u2502 " + titulo + " \u2502")
    print("\u2570" + "\u2500" * (len(titulo) + 2) + "\u256f\n")