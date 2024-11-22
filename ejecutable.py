from clases import *

def pedir_mostrar_cadena():
    print("Ingresa la cadena de ADN por filas:")
    centinela = True
    cadena_adn = []
    while centinela:
        cadena_adn = []
        for i in range(6):
            while True:
                fila = str(input(f"Fila {i + 1}: ")).upper()
                fila.split()
                if all(base in ["A", "C", "G", "T"] for base in fila) and len(fila) == 6:
                    cadena_adn.append(fila)
                    break
                else:
                    print("Error: Solo se permiten las bases A, C, G y T, y cada fila debe tener exactamente 6 bases.")
        print("La cadena ingresada es:")
        for j in range(6):
            print(f"{cadena_adn[j]}\n")
        try:
            op = input("Es correcta esta cadena?: [S/N]: ").lower()
            if op == "s":
                centinela = False
            elif op != "n":
                raise ValueError("Opción no válida. Debes ingresar 'S' o 'N'.")
        except ValueError as e:
            print(f"Error {e}")
    return cadena_adn

def menu():
    try:
        print("""
            ****Cadenas De ADN****
Menu: [Una vez ingreses la cadena de ADN se desbloquearan opciones nuevas]
1. Ingresar cadena de ADN

""")
        op = str(input("Ingresa una opcion: "))
        if op == "1":  # Cambiar '1' a cadena
            adn = pedir_mostrar_cadena()
            menu_adn(adn)
        else:
            raise ValueError("Opcion no valida por el momento primero ingresa la cadena de ADN para mostrar las otras opciones")
    except ValueError as e:
        print(f"Error: {e}")

def menu_adn(adn):
    try:
        while True:
            print("""\n
2. Detectar mutaciones
3. Mutar ADN
4. Sanar ADN
5. Salir

""")
            # hasta aca adn es la variable donde se tiene guardada la matriz
            try:
                op = int(input("Dime que quieres hacer? [2|3|4|5]: "))
                if op == 2:
                    detector = Detector(adn)
                    detectar_mutacion = detector.detectar_mutaciones(adn)
                    print(f"\nResultados de la detección: {detectar_mutacion}")
                elif op == 3:
                    #---------------------- MUTADOR --------------------------
                    print("\nInicia el proceso de mutación...")

                    # pedir y valida base nitrogenada
                    while True:
                        base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, C, G, T): ").strip().upper()
                        if base_nitrogenada in ["A", "C", "G", "T"]:
                            break
                        else:
                            print("Error: La base nitrogenada debe ser 'A', 'C', 'G' o 'T'. Intenta nuevamente.")

                    # pedir y validar intensidad de mutacion
                    while True:
                        try:
                            intensidad_mutacion = int(input("Ingrese la intensidad de la mutación (4, 5, 6): ").strip())
                            if intensidad_mutacion in [4, 5, 6]:
                                break
                            else:
                                print("Error: La intensidad debe ser 4, 5 o 6. Intenta nuevamente.")
                        except ValueError:
                            print("Error: Debes ingresar un número entero. Intenta nuevamente.")

                    # elegir si la mutacion sera radiacion o virus
                    while True:
                        tipo_mutacion = input("¿Qué tipo de mutación deseas aplicar? (Radiacion o Virus): ").strip().lower()
                        if tipo_mutacion in ["radiacion", "virus"]:
                            break
                        else:
                            print("Error: Debes ingresar 'Radiacion' o 'Virus'. Intenta nuevamente.")

                    # Aplicar mutación según el tipo
                    if tipo_mutacion == "radiacion":
                        while True:
                            direccion = input("¿En qué dirección deseas realizar la mutación? (horizontal o vertical): ").strip().lower()
                            if direccion in ["horizontal", "vertical"]:
                                break
                            else:
                                print("Error: Debes ingresar 'horizontal' o 'vertical'. Intenta nuevamente.")

                        mutacion = Radiacion(adn, base_nitrogenada, intensidad_mutacion, direccion)

                    elif tipo_mutacion == "virus":
                        mutacion = Virus(adn, base_nitrogenada, intensidad_mutacion)

                    # Aplicar la mutación desde la posición inicial (0, 0)
                    resultado_mut = mutacion.crear_mutante((0, 0))

                    
                    # Establecer mutacion en TRUE
                    detector = Detector(adn)
                    detector.mutacion = True
                    adn = resultado_mut
                    
                    # Mostrar el resultado de la mutación
                    print("\nResultados de la mutación:")
                    for fila in resultado_mut:
                        print(' '.join(fila))


                    #---------------------- MUTADOR --------------------------

                elif op == 4:
                    # detectar si hay mutaciones y establecer estado en True o False
                    detector = Detector(adn)
                    detectar_mutacion = detector.detectar_mutaciones(adn)
                    
                    isMutant = detector.mutacion
                    cadena = Sanador(adn, isMutant)

                    adn_mutado = cadena.adn
                    
                    print("\nADN actual:\n")
                    for fila in cadena.adn:
                        print(' '.join(fila))

                    if cadena.mutada == True:
                        adn_sano = cadena.sanar_mutacion(adn_mutado)
                    else:
                        print("\n>> SU ADN YA ESTÁ SANO, POR LO QUE NO ES NECESARIO SANARLO NUEVAMENTE <<")

                    cadena.adn = adn_sano
                    adn = cadena.adn
                    # establecer estado de mutacion en False
                    detector.mutacion = cadena.mutada

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

main()
