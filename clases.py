import random

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


class Mutador:
    pass

class Radiacion(Mutador):
    pass

class Virus(Mutador):
    pass

class Sanador:
    def __init__(self, adn, mutada):
        self.adn = adn
        self.mutada = mutada

    def sanar_mutacion(self, adn):
        adn_sanado = []
        for i in range(6):
            adn[i] = list(adn[i])
            random.shuffle(adn[i])
            adn[i] = ''.join(adn[i])
        
        while Detector.detectar_diagonal(self, adn) or Detector.detectar_horizontal(self, adn) or Detector.detectar_vertical(self, adn):
            for i in range(6):
                adn[i] = list(adn[i])
                random.shuffle(adn[i])
                adn[i] = ''.join(adn[i])
                
        self.mutada = False
        return adn
