import random
import string

class Detector:
    """
        Clase Detector encargada de detectar mutaciones en una matriz de ADN.

        Atributos:
        mutacion (bool): Indica si se ha detectado una mutación.
        mensaje (str): Mensaje descriptivo de la mutación detectada.
        matriz (list[str]): Matriz de ADN a analizar.
        coordenadas_mutacion (list[tuple[int, int]]): Coordenadas de la mutación detectada.
        """
    mutacion: bool = False
    mensaje: str = ""
    def __init__(self, matriz: list[str]) -> None:
        """
        Inicializa el Detector con una matriz de ADN.

        Parámetros:
                matriz (list[str]): Matriz de ADN representada como una lista de cadenas,
                                    donde cada cadena representa una fila de ADN.

        Retorna: None
                """
        self.matriz: list[str] = matriz
        self.coordenadas_mutacion: list[tuple[int, int]] = []
    def detectar_horizontal(self, matriz: list[str]) -> bool | tuple[bool, list[tuple[int, int]], str]:
        """
                Detecta mutaciones horizontales en la matriz de ADN.

                Parámetros:
                matriz (list[str]): Matriz de ADN representada como una lista de cadenas.

                Retorna:
                bool | tuple[bool, list[tuple[int, int]], str]:
                    - Si se detecta una mutación, retorna un tuple con:
                        - un valor booleano `True` indicando que se detectó una mutación.
                        - las coordenadas de la mutación (lista de tuplas con las posiciones de la mutación).
                        - un mensaje describiendo la mutación detectada.
                    - Si no se detecta mutación, retorna `False`.
                """
        try:
            filas: int = len(matriz)
            columnas: int = len(matriz[0])
            for i in range(filas):
                for j in range(columnas - 3):
                    secuencia: list[str] = [matriz[i][j], matriz[i][j + 1], matriz[i][j + 2], matriz[i][j + 3]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        self.mutacion: bool = True
                        self.coordenadas_mutacion: list[tuple[int, int]] = [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]
                        self.mensaje: str = f"Mutacion horizontal:{secuencia}"
                        return self.mutacion, self.coordenadas_mutacion, self.mensaje
            self.mutacion: bool = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_horizontal: {e}")

    def detectar_vertical(self, matriz: list[str]) -> bool | tuple[bool, list[tuple[int, int]], str]:
        """
               Detecta mutaciones verticales en la matriz de ADN.

               Parámetros:
               matriz (list[str]): Matriz de ADN representada como una lista de cadenas.

               Retorna:
               bool | tuple[bool, list[tuple[int, int]], str]:
                   - Si se detecta una mutación, retorna un tuple con:
                       - un valor booleano `True` indicando que se detectó una mutación.
                       - las coordenadas de la mutación (lista de tuplas con las posiciones de la mutación).
                       - un mensaje describiendo la mutación detectada.
                   - Si no se detecta mutación, retorna `False`.
               """
        try:
            filas: int = len(matriz)
            columnas: int = len(matriz[0])
            for j in range(columnas):
                for i in range(filas - 3):
                    secuencia: list[str] = [matriz[i][j], matriz[i + 1][j], matriz[i + 2][j], matriz[i + 3][j]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        self.mutacion: bool = True
                        self.coordenadas_mutacion: list[tuple[int, int]] = [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]
                        self.mensaje: str = f"Mutacion Vertical:{secuencia}"
                        return self.mutacion, self.coordenadas_mutacion, self.mensaje
            self.mutacion: bool = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_vertical: {e}")

    def detectar_diagonal_descendente(self, matriz: list[str]) -> bool | tuple[bool, list[tuple[int, int]], str]:
        """
                Detecta mutaciones diagonales descendentes en la matriz de ADN.

                Parámetros:
                matriz (list[str]): Matriz de ADN representada como una lista de cadenas.

                Retorna:
                bool | tuple[bool, list[tuple[int, int]], str]:
                    - Si se detecta una mutación, retorna un tuple con:
                        - un valor booleano `True` indicando que se detectó una mutación.
                        - las coordenadas de la mutación (lista de tuplas con las posiciones de la mutación).
                        - un mensaje describiendo la mutación detectada.
                    - Si no se detecta mutación, retorna `False`.
                """
        try:
            filas: int = len(matriz)
            columnas: int = len(matriz[0])
            for i in range(filas - 3):
                for j in range(columnas - 3):
                    secuencia: list[str] = [matriz[i][j], matriz[i + 1][j + 1], matriz[i + 2][j + 2],
                                            matriz[i + 3][j + 3]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        self.mutacion: bool = True
                        self.coordenadas_mutacion: list[tuple[int, int]] = [(i, j), (i + 1, j + 1), (i + 2, j + 2),
                                                                            (i + 3, j + 3)]
                        self.mensaje: str = f"Mutacion Diagonal:{secuencia}"
                        return self.mutacion, self.coordenadas_mutacion, self.mensaje
            self.mutacion: bool = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_diagonal: {e}")

    def detectar_diagonal_ascendente(self, matriz: list[str]) -> bool | tuple[bool, list[tuple[int, int]], str]:
        """
                Detecta mutaciones diagonales ascendentes en la matriz de ADN.

                Parámetros:
                matriz (list[str]): Matriz de ADN representada como una lista de cadenas.

                Retorna:
                bool | tuple[bool, list[tuple[int, int]], str]:
                    - Si se detecta una mutación, retorna un tuple con:
                        - un valor booleano `True` indicando que se detectó una mutación.
                        - las coordenadas de la mutación (lista de tuplas con las posiciones de la mutación).
                        - un mensaje describiendo la mutación detectada.
                    - Si no se detecta mutación, retorna `False`.
                """
        try:
            filas: int = len(matriz)
            columnas: int = len(matriz[0])
            for i in range(filas - 3):
                for j in range(3, columnas):
                    secuencia: list[str] = [matriz[i][j], matriz[i + 1][j - 1], matriz[i + 2][j - 2], matriz[i + 3][j - 3]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        self.mutacion: bool = True
                        self.coordenadas_mutacion: list[tuple[int, int]] = [(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)]
                        self.mensaje: str = f"Mutacion Diagonal:{secuencia}"
                        return self.mutacion, self.coordenadas_mutacion, self.mensaje
            self.mutacion: bool = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_diagonal: {e}")

    def detectar_mutaciones(self, matriz: list[str]) -> str | tuple[bool, list[tuple[int, int]], str]:
        """
                Detecta mutaciones en todas las direcciones (horizontal, vertical y diagonal) en la matriz de ADN.

                Parámetros:
                matriz (list[str]): Matriz de ADN representada como una lista de cadenas.

                Retorna:
                str | tuple[bool, list[tuple[int, int]], str]:
                    - Si se detecta una mutación, retorna un tuple con:
                        - un valor booleano `True` indicando que se detectó una mutación.
                        - las coordenadas de la mutación (lista de tuplas con las posiciones de la mutación).
                        - un mensaje describiendo la mutación detectada.
                    - Si no se detecta mutación, retorna el mensaje 'No se detectaron mutaciones'.
                """
        try:
            if self.detectar_horizontal(matriz):
                return self.mutacion, self.coordenadas_mutacion, self.mensaje
            elif self.detectar_vertical(matriz):
                return self.mutacion, self.coordenadas_mutacion, self.mensaje
            elif self.detectar_diagonal_descendente(matriz):
                return self.mutacion, self.coordenadas_mutacion, self.mensaje
            elif self.detectar_diagonal_ascendente(matriz):
                return self.mutacion, self.coordenadas_mutacion, self.mensaje
            else:
                return "No se detectaron mutaciones en la matriz."
        except Exception as e:
            return f"Error en detectar_mutaciones: {self.mensaje if self.mensaje else str(e)}"
        finally:
            print("Método detectar_mutaciones finalizado.")

    def __str__(self) -> str:
        if self.mutacion:
            return f"Mutacion encontrada{self.mensaje}"
        else:
            return f"No se detecto ninguna mutacion"


#---------------------------------clase mutador------------------------------------------------------------------

class Mutador:
    def __init__(self, matriz_adn: list[list[str]], base_nitrogenada: str, intensidad_mutacion: int):
        """
        Clase base para aplicar mutaciones en una matriz de ADN.

        Args:
            matriz_adn (list[list[str]]): La matriz de ADN a ser mutada.
            base_nitrogenada (str): Base nitrogenada que reemplazará en las mutaciones (ejemplo: 'A', 'T').
            intensidad_mutacion (int): Cantidad de posiciones que serán afectadas por la mutación.
        """
        self.matriz_adn: list[list[str]] = matriz_adn
        self.base_nitrogenada: str = base_nitrogenada
        self.intensidad_mutacion: int = intensidad_mutacion
        self.posicion_mutacion: tuple[int, int] = (0, 0)  # Siempre comienza desde (0, 0)

    def crear_mutante(self, posicion_inicial: tuple[int, int]) -> None:
        """
        Metodo a ser implementado en las clases hijas para aplicar mutaciones específicas.

        Args:
            posicion_inicial (tuple[int, int]): coordenadas de inicio de la mutacion (fila, columna).
        """
        pass



    
    
# ----------------------------Clase Radiacion -----------------------------------------
class Radiacion(Mutador):
    """
    Clase que aplica mutaciones de tipo radiación a una matriz de ADN.

    La radiación muta las bases nitrogenadas de la matriz en una dirección específica
    ("horizontal" o "vertical"), comenzando desde una posición inicial y propagándose
    según la intensidad de mutación especificada.

    Hereda de:
        Mutador

    Atributos:
        matriz_adn (list[str]): La matriz de ADN a modificar.
        base_nitrogenada (str): La base nitrogenada que se usará para realizar la mutación.
        intensidad_mutacion (int): Cantidad de bases consecutivas que serán mutadas.
        direccion (str): Dirección de la mutación ("horizontal" o "vertical").
    """

    def __init__(self, matriz_adn: list[str], base_nitrogenada: str, intensidad_mutacion: int, direccion: str):
        """
        Inicializa la clase Radiacion con los parámetros específicos.

        :param matriz_adn: Lista de cadenas que representan el ADN.
        :param base_nitrogenada: Base nitrogenada a aplicar en la mutación.
        :param intensidad_mutacion: Número de posiciones consecutivas a modificar.
        :param direccion: Dirección de la mutación ('horizontal' o 'vertical').
        """
        super().__init__(matriz_adn, base_nitrogenada, intensidad_mutacion)
        self.direccion = direccion

    def crear_mutante(self, posicion_inicial: tuple[int, int]) -> list[str]:
        """
        Aplica la mutación de radiación en la matriz de ADN.

        Realiza la mutación desde una posición inicial en la dirección especificada,
        modificando las bases nitrogenadas según la intensidad.

        :param posicion_inicial: Tupla con las coordenadas iniciales de la mutación (fila, columna).
        :return: La matriz de ADN mutada.
        :raises IndexError: Si la posición inicial está fuera de los límites de la matriz.
        :raises ValueError: Si ocurre un error inesperado durante la mutación.
        """
        try:
            fila, columna = posicion_inicial

            # Validar que la posición inicial está dentro de los límites de la matriz.
            if not (0 <= fila < len(self.matriz_adn)) or not (0 <= columna < len(self.matriz_adn[0])):
                raise IndexError("La posición inicial está fuera de los límites de la matriz de ADN.")

            # Convertir las filas de la matriz a listas para permitir modificaciones.
            for i in range(len(self.matriz_adn)):
                self.matriz_adn[i] = list(self.matriz_adn[i])

            # Aplicar la mutación según la intensidad y la dirección.
            for _ in range(self.intensidad_mutacion):
                self.matriz_adn[fila][columna] = self.base_nitrogenada

                if self.direccion == "horizontal":
                    columna += 1
                    if columna >= len(self.matriz_adn[0]):
                        break  # Evitar desbordar la matriz horizontalmente.
                elif self.direccion == "vertical":
                    fila += 1
                    if fila >= len(self.matriz_adn):
                        break  # Evitar desbordar la matriz verticalmente.

            # Convertir las filas de nuevo a cadenas.
            for i in range(len(self.matriz_adn)):
                self.matriz_adn[i] = ''.join(self.matriz_adn[i])

            return self.matriz_adn

        except IndexError as e:
            print(f"Error: {e}")
            raise  # Re-lanzar la excepción para que el llamador decida cómo manejarla.

        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            raise ValueError("Error en la mutación de radiación.") from e


#----------------------------------- virus --------------------------------------
class Virus(Mutador):
    """
    Clase para realizar mutaciones por virus en la diagonal principal o secundaria de una matriz de ADN.
    """

    def __init__(self, matriz_adn: list[str], base_nitrogenada: str, intensidad_mutacion: int):
        """
        Inicializa la clase Virus con los parámetros específicos.

        :param matriz_adn: Lista de cadenas que representan el ADN.
        :param base_nitrogenada: Base nitrogenada que será aplicada en la mutación.
        :param intensidad_mutacion: Número de posiciones a modificar en la diagonal.
        """
        # Convertir las filas de la matriz a listas para permitir modificaciones
        matriz_convertida = [list(fila) for fila in matriz_adn]
        super().__init__(matriz_convertida, base_nitrogenada, intensidad_mutacion)

    def crear_mutante(self, posicion_inicial: tuple[int, int]) -> list[list[str]]:
        """
        Realiza la mutación del ADN en la diagonal principal o secundaria desde la posición inicial.

        :param posicion_inicial: Tupla con las coordenadas iniciales (fila, columna).
        :return: La matriz de ADN mutada como lista de listas.
        """
        try:
            # Preguntar al usuario la dirección de la mutación
            direccion = input("¿Desea que el virus se extienda en forma descendente (diagonal principal) o ascendente (diagonal secundaria)? (descendente/ascendente): ").strip().lower()
            fila, columna = posicion_inicial

            # Validar la entrada del usuario
            if direccion not in ["descendente", "ascendente"]:
                print("Opción inválida. Se usará la extensión descendente (diagonal principal) por defecto.")
                direccion = "descendente"

            # Aplicar la mutación en la diagonal correspondiente
            for i in range(self.intensidad_mutacion):
                if direccion == "descendente":  # Diagonal principal
                    if 0 <= fila + i < len(self.matriz_adn) and 0 <= columna + i < len(self.matriz_adn[0]):
                        self.matriz_adn[fila + i][columna + i] = self.base_nitrogenada
                elif direccion == "ascendente":  # Diagonal secundaria
                    if 0 <= fila + i < len(self.matriz_adn) and 0 <= columna - i < len(self.matriz_adn[0]):
                        self.matriz_adn[fila + i][columna - i] = self.base_nitrogenada

            return self.matriz_adn

        except Exception as e:
            print(f"Error al realizar la mutación: {e}")
            return self.matriz_adn  # Devuelve la matriz sin cambios en caso de error




#--------------------------------- Sanador --------------------------------------

class Sanador(Detector):
    """
    Clase para sanar mutaciones en una matriz de ADN.
    """

    def __init__(self, adn: list[str], mutada: bool):
        """
        Inicializa la clase Sanador con el estado del ADN y su estado de mutacion.

        :param adn: Lista de cadenas que representan el ADN.
        :param mutada: Indica si el ADN contiene mutaciones (True) o no (False).
        """
        self.adn = adn
        self.mutada = mutada

    def sanar_mutacion(self, adn: list[str]) -> list[str]:
        """
        Corrige las mutaciones en el ADN reemplazando las letras de manera aleatoria
        hasta que no se detecten mutaciones.

        :param adn: Lista de cadenas que representan el ADN mutado.
        :return: ADN sano como lista de cadenas.
        """
        # Letras validas para el ADN
        nuevas_letras = ['A', 'T', 'C', 'G']

        if self.mutada:
            try:
                # Reemplazar cada letra por una aleatoria
                for i in range(len(adn)):
                    adn[i] = ''.join(random.choice(nuevas_letras) for _ in range(len(adn[i])))

                # Repetir hasta que no haya mutaciones detectadas
                while (
                    Detector.detectar_diagonal_ascendente(self, adn) or
                    Detector.detectar_diagonal_descendente(self, adn) or
                    Detector.detectar_horizontal(self, adn) or
                    Detector.detectar_vertical(self, adn)
                ):
                    for i in range(len(adn)):
                        adn[i] = ''.join(random.choice(nuevas_letras) for _ in range(len(adn[i])))

                # Mostrar el ADN sano
                print("\n\nADN sano:\n")
                for fila in adn:
                    print(' '.join(fila))

                self.mutada = False
            except ValueError as e:
                print(f"Error: {e}")

        return adn
