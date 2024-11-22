from clases import *

def pedir_mostrar_cadena() -> list[list[str]]:
    """
    Solicita al usuario ingresar una matriz de ADN, validando que cumpla con las reglas establecidas,
    y muestra la matriz ingresada para confirmación.

    Retorna:
        list[list[str]]: Matriz de ADN ingresada por el usuario, representada como una lista de listas de cadenas.
    """
    print("Ingresa la cadena de ADN por filas:")
    centinela: bool = True
    cadena_adn: list[list[str]] = []
    while centinela:
        cadena_adn = []
        for i in range(6):
            while True:
                fila: str = input(f"Fila {i + 1}: ").upper()
                if all(base in ["A", "C", "G", "T"] for base in fila) and len(fila) == 6:
                    cadena_adn.append(list(fila))
                    break
                else:
                    print("Error: Solo se permiten las bases A, C, G y T, y cada fila debe tener exactamente 6 bases.")
        print("La cadena ingresada es:")
        for j in range(6):
            print(" ".join(cadena_adn[j]))
        try:
            op: str = input("¿Es correcta esta cadena? [S/N]: ").lower()
            if op == "s":
                centinela = False
            elif op != "n":
                raise ValueError("Opción no válida. Debes ingresar 'S' o 'N'.")
        except ValueError as e:
            print(f"Error {e}")
    return cadena_adn

def menu() -> None:
    """
    Muestra el menú principal del programa para ingresar una cadena de ADN.
    Al ingresar la cadena, se habilitan opciones adicionales.
    """
    try:
        print("""
            **** Cadenas De ADN ****
Menu: [Una vez ingreses la cadena de ADN se desbloquearan opciones nuevas]
1. Ingresar cadena de ADN

""")
        op: str = input("Ingresa una opción: ")
        if op == "1":
            adn: list[list[str]] = pedir_mostrar_cadena()
            menu_adn(adn)
        else:
            raise ValueError("Opción no válida por el momento. Primero ingresa la cadena de ADN para mostrar las otras opciones.")
    except ValueError as e:
        print(f"Error: {e}")

def menu_adn(adn: list[list[str]]) -> None:
    """
    Muestra el menú secundario del programa con opciones para trabajar con la cadena de ADN ingresada.

    Parámetros:
        adn (list[list[str]]): Matriz de ADN representada como una lista de listas de cadenas.
    """
    try:
        while True:
            print("""\n
2. Detectar mutaciones
3. Mutar ADN
4. Sanar ADN
5. Salir

""")
            try:
                op: int = int(input("Dime qué quieres hacer? [2|3|4|5]: "))
                if op == 2:
                    detector: Detector = Detector(adn)
                    detectar_mutacion: str = detector.detectar_mutaciones(adn)
                    print(f"\nResultados de la detección: {detectar_mutacion}")
                elif op == 3:
                    print("\nInicia el proceso de mutación...")
                    while True:
                        base_nitrogenada: str = input("Ingrese la base nitrogenada para la mutación (A, C, G, T): ").strip().upper()
                        if base_nitrogenada in ["A", "C", "G", "T"]:
                            break
                        else:
                            print("Error: La base nitrogenada debe ser 'A', 'C', 'G' o 'T'. Intenta nuevamente.")

                    while True:
                        try:
                            intensidad_mutacion: int = int(input("Ingrese la intensidad de la mutación (4, 5, 6): ").strip())
                            if intensidad_mutacion in [4, 5, 6]:
                                break
                            else:
                                print("Error: La intensidad debe ser 4, 5 o 6. Intenta nuevamente.")
                        except ValueError:
                            print("Error: Debes ingresar un número entero. Intenta nuevamente.")

                    while True:
                        tipo_mutacion: str = input("¿Qué tipo de mutación deseas aplicar? (Radiacion o Virus): ").strip().lower()
                        if tipo_mutacion in ["radiacion", "virus"]:
                            break
                        else:
                            print("Error: Debes ingresar 'Radiacion' o 'Virus'. Intenta nuevamente.")

                    if tipo_mutacion == "radiacion":
                        while True:
                            direccion: str = input("¿En qué dirección deseas realizar la mutación? (horizontal o vertical): ").strip().lower()
                            if direccion in ["horizontal", "vertical"]:
                                break
                            else:
                                print("Error: Debes ingresar 'horizontal' o 'vertical'. Intenta nuevamente.")

                        mutacion: Radiacion = Radiacion(adn, base_nitrogenada, intensidad_mutacion, direccion)

                    elif tipo_mutacion == "virus":
                        mutacion: Virus = Virus(adn, base_nitrogenada, intensidad_mutacion)

                    resultado_mut: list[list[str]] = mutacion.crear_mutante((0, 0))
                    detector: Detector = Detector(adn)
                    detector.mutacion = True
                    adn = resultado_mut

                    print("\nResultados de la mutación:")
                    for fila in resultado_mut:
                        print(" ".join(fila))

                elif op == 4:
                    detector: Detector = Detector(adn)
                    is_mutant: bool = detector.detectar_mutaciones(adn)
                    sanador: Sanador = Sanador(adn, is_mutant)

                    if sanador.mutada:
                        adn = sanador.sanar_mutacion(sanador.adn)
                    else:
                        print("\n>> SU ADN YA ESTÁ SANO, POR LO QUE NO ES NECESARIO SANARLO NUEVAMENTE <<")

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

def main() -> None:
    """
    Función principal que inicia el programa mostrando el menú principal.
    """
    menu()

main()
