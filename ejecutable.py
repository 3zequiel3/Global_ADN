from clases import *

def pedir_mostrar_cadena():
    print("Ingresa la cadena de ADN por filas:")
    centinela = True
    cadena_adn = []
    while centinela:
        cadena_adn = []
        for i in range(6):
            fila = str(input(f"Fila {i + 1}: ")).split()
            cadena_adn.append(fila)
        print("La cadena ingresada es:")
        for j in range(6):
            print(f"{cadena_adn[j]}\n")

        try:
            op = input("Es correcta esta cadena?: [S/N]").lower()
            if op == "s":
                centinela = False
            elif op != "n":
                raise ValueError("Opción no válida. Debes ingresar 'S' o 'N'.")
        except ValueError as e:
            print(e)
    return cadena_adn

def menu():
    try:
        print("""
            ****Cadenas De ADN****
            Menu: [Una vez ingreses la cadena de ADN se desbloquearan opciones nuevas]
            1. Ingresar cadena de ADN""")
        op = input("Ingresa una opcion: ")
        if op == "1":  # Cambiar '1' a cadena
            adn = pedir_mostrar_cadena()
            menu_adn(adn)
        else:
            raise ValueError("Opcion no valida por el momento primero ingresa la cadena de ADN para mostrar las otras opciones")
    except ValueError as e:
        print(f"Error: {e}")

def menu_adn(adn):
    print("""
    2. Detectar mutaciones
    3. Mutar ADN
    4. Sanar ADN
    5. Salir""")
    try:
        while True:
            print("""
                   2. Detectar mutaciones
                   3. Mutar ADN
                   4. Sanar ADN
                   5. Salir""")
            try:
                op = int(input("Dime que quieres hacer? [2|3|4|5]: "))
                if op == 2:
                    detector = Detector(adn)
                    detectar_mutacion = detector.detectar_mutaciones(adn)
                    print(f"\nResultados de la detección: {detectar_mutacion}")
                elif op == 3:
                    # Aquí va la logica para mutar ADN
                    pass
                elif op == 4:
                    # Aquí va la logica para sanar ADN
                    pass
                elif op == 5:
                    print("Saliendo del programa...")
                    break
                else:
                    raise ValueError("Opción no válida. Por favor, selecciona una opción del menú.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
    except Exception as e:
        print(f"Error inesperado en el menú ADN: {e}")
    finally:
        print("Programa Finalizado")

def main():
    menu()
