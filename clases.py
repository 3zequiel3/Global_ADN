import random
import string

class Detector:
    mutacion: bool = False
    mensaje = ""
    def __init__(self,matriz):
        self.matriz = matriz
        self.coordenadas_mutacion = []
    def detectar_horizontal(self,matriz):
        try:
            filas = len(matriz)
            columnas = len(matriz[0])
            for i in range(filas):
                for j in range(columnas - 3):
                    secuencia = [matriz[i][j], matriz[i][j + 1], matriz[i][j + 2], matriz[i][j + 3]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        self.mutacion = True
                        self.coordenadas_mutacion = [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]
                        self.mensaje = f"Mutacion horizontal:{secuencia}"
                        return self.mutacion,self.coordenadas_mutacion, self.mensaje
            self.mutacion = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_horizontal: {e}")

    def detectar_vertical(self,matriz):
        try:
            filas = len(matriz)
            columnas = len(matriz[0])
            for j in range(columnas):
                for i in range(filas - 3):
                    secuencia = [matriz[i][j], matriz[i + 1][j], matriz[i + 2][j], matriz[i + 3][j]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        self.mutacion = True
                        self.coordenadas_mutacion = [(i,j),(i+1,j),(i+2,j),(i+3,j)]
                        self.mensaje = f"Mutacion Vertical:{secuencia}"
                        return self.mutacion,self.coordenadas_mutacion, self.mensaje
            self.mutacion = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_vertical: {e}")


    def detectar_diagonal_descendente(self,matriz):
        try:
            filas = len(matriz)
            columnas = len(matriz[0])
            for i in range(filas - 3):
                for j in range(columnas - 3):
                    secuencia = [matriz[i][j], matriz[i + 1][j + 1], matriz[i + 2][j + 2], matriz[i + 3][j + 3]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        #diagonal descendente
                        self.mutacion = True
                        self.coordenadas_mutacion = [(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)]
                        self.mensaje = f"Mutacion Diagonal:{secuencia}"
                        return self.mutacion, self.coordenadas_mutacion, self.mensaje
            self.mutacion = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_diagonal: {e}")

    def detectar_diagonal_ascendente(self,matriz):
        try:
            filas = len(matriz)
            columnas = len(matriz[0])
            for i in range(filas - 3):
                for j in range(3,columnas):
                    secuencia = [matriz[i][j], matriz[i + 1][j - 1], matriz[i + 2][j - 2], matriz[i + 3][j - 3]]
                    if secuencia[0] == secuencia[1] == secuencia[2] == secuencia[3]:
                        # diagonal descendente
                        self.mutacion = True
                        self.coordenadas_mutacion = [(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)]
                        self.mensaje = f"Mutacion Diagonal:{secuencia}"
                        return self.mutacion, self.coordenadas_mutacion, self.mensaje
            self.mutacion = False
            return self.mutacion
        except IndexError:
            print("Error: La cadena de ADN no tiene las dimensiones adecuadas para detectar mutaciones.")
        except Exception as e:
            print(f"Error inesperado en detectar_diagonal: {e}")

    def detectar_mutaciones(self,matriz):
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
        except Exception as e :
             return f"Error en detectar_mutaciones: {self.mensaje if self.mensaje else str(e)}"
        finally:
            print("Método detectar_mutaciones finalizado.")

    def __str__(self):
        if self.mutacion:
            return f"Mutacion encontrada{self.mensaje}"
        else:
            return f"No se detecto ninguna mutacion"


#--------------------------------------------------------------------------------------------------------
#Mutador
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


#--------------------------------------------------------------------------------------------------------
    
    
    
# ----------------------  nueva Clase Radiacion -----------------------------------
class Radiacion(Mutador):
    """
    Clase para realizar mutaciones por radiación en una matriz de ADN.
    La mutación puede ser en dirección horizontal o vertical.
    """

    def __init__(self, matriz_adn: list[str], base_nitrogenada: str, intensidad_mutacion: int, direccion: str):
        """
        inicializa la clase Radiacion con los parametros especificos

        :param matriz_adn: lista de cadenas que representan el ADN
        :param base_nitrogenada: base nitrogenada a aplicar en la mutacion
        :param intensidad_mutacion: numero de posiciones a modificar
        :param direccion: direccion de la mutacion ('horizontal' o 'vertical')
        """
        super().__init__(matriz_adn, base_nitrogenada, intensidad_mutacion)
        self.direccion = direccion

    def crear_mutante(self, posicion_inicial: tuple[int, int]) -> list[str]:
        """
        realiza la mutacion del ADN desde la posicion inicial en la direccion especificaad

        :param posicion_inicial: tupla con las coordenadas iniciales (fila, columna)
        :return: La matriz de ADN mutada
        """
        fila, columna = posicion_inicial

        # convertir las filas de la matriz a listas para permitir modificaciones
        for i in range(len(self.matriz_adn)):
            self.matriz_adn[i] = list(self.matriz_adn[i])

        for _ in range(self.intensidad_mutacion):
            self.matriz_adn[fila][columna] = self.base_nitrogenada

            # modificar segun la direccion
            if self.direccion == "horizontal":
                columna += 1
                if columna >= len(self.matriz_adn[0]):
                    break  # evitar desbordar la matriz horizontalmente
            elif self.direccion == "vertical":
                fila += 1
                if fila >= len(self.matriz_adn):
                    break  # evitar desbordar la matriz verticalmente

        # Convertir las filas de nuevo a strings
        for i in range(len(self.matriz_adn)):
            self.matriz_adn[i] = ''.join(self.matriz_adn[i])

        return self.matriz_adn


    
    
    
#----------------------------------- nueva clase radiacion --------------------------------------




#----------------------------------- virus --------------------------------------
class Virus(Mutador):
    """
    Clase para realizar mutaciones por virus en la diagonal principal de una matriz de ADN.
    """

    def __init__(self, matriz_adn: list[str], base_nitrogenada: str, intensidad_mutacion: int):
        """
        Inicializa la clase Virus con los parametros especificos.

        :param matriz_adn: Lista de cadenas que representan el ADN.
        :param base_nitrogenada: Base nitrogenada que sera aplicada en la mutacion.
        :param intensidad_mutacion: Numero de posiciones a modificar en la diagonal principal.
        """
        # Convertir las filas de la matriz a listas para permitir modificaciones
        matriz_convertida = [list(fila) for fila in matriz_adn]
        super().__init__(matriz_convertida, base_nitrogenada, intensidad_mutacion)

    def crear_mutante(self, posicion_inicial: tuple[int, int]) -> list[list[str]]:
        """
        Realiza la mutacion del ADN en la diagonal principal desde la posicion inicial.

        :param posicion_inicial: Tupla con las coordenadas iniciales (fila, columna).
        :return: La matriz de ADN mutada como lista de listas.
        """
        fila, columna = posicion_inicial

        # Aplicar la mutacion en la diagonal principal
        for i in range(self.intensidad_mutacion):
            if 0 <= fila + i < len(self.matriz_adn) and 0 <= columna + i < len(self.matriz_adn[0]):
                self.matriz_adn[fila + i][columna + i] = self.base_nitrogenada
        return self.matriz_adn





#----------------------------------- virus --------------------------------------


import random

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
