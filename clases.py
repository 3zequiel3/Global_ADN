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
    def __init__(self, matriz_adn, base_nitrogenada, intensidad_mutacion):
        self.matriz_adn = matriz_adn
        self.base_nitrogenada = base_nitrogenada
        self.intensidad_mutacion = intensidad_mutacion
        self.posicion_mutacion = (0, 0)  # Siempre comienza desde (0, 0)


    def crear_mutante(self, posicion_inicial):
        # metodo vacio para ser usado en las clases hijas
        pass



#--------------------------------------------------------------------------------------------------------

# class Radiacion(Mutador):
    
    #   Esto lo habia escrito Enzo
    
    # def __init__(self, adn):
    #     """
    #     Constructor de la clase Radiacion.
    #     :param adn: La matriz de ADN que se va a mutar.
    #     """
    #     super().__init__(adn)

    # def crear_mutante(self, posicion_inicial, orientacion_de_la_mutacion):
    #     """
    #     Crea un mutante en la matriz dependiendo de la orientación (horizontal o vertical)
    #     y genera 4 bases nitrogenadas 'T' consecutivas en la posición inicial.
    #     :param posicion_inicial: La posición donde empieza la mutación (tupla de fila, columna).
    #     :param orientacion_de_la_mutacion: Dirección de la mutación: "horizontal" o "vertical".
    #     :return: La matriz de ADN mutada.
    #     """
    #     base_nitrogenada = 'T'

    #     # Creamos una copia de la matriz para no modificar la original
    #     matriz_mutada = [fila[:] for fila in self.adn]

    #     # Validamos la orientación
    #     if orientacion_de_la_mutacion == "horizontal":
    #         fila, columna = posicion_inicial
    #         # Verificar si hay espacio para las 4 bases 'T' consecutivas
    #         if 0 <= fila < 6 and 0 <= columna < 6 and columna + 3 < 6:
    #             # Colocamos las 4 bases 'T' consecutivas
    #             for i in range(columna, columna + 4):
    #                 matriz_mutada[fila][i] = base_nitrogenada
    #         else:
    #             raise ValueError("No hay suficiente espacio horizontal para colocar 4 bases 'T' consecutivas.")

    #     elif orientacion_de_la_mutacion == "vertical":
    #         fila, columna = posicion_inicial
    #         # Verificar si hay espacio para las 4 bases 'T' consecutivas
    #         if 0 <= columna < 6 and 0 <= fila < 6 and fila + 3 < 6:
    #             # Colocamos las 4 bases 'T' consecutivas
    #             for i in range(fila, fila + 4):
    #                 matriz_mutada[i][columna] = base_nitrogenada
    #         else:
    #             raise ValueError("No hay suficiente espacio vertical para colocar 4 bases 'T' consecutivas.")

    #     else:
    #         raise ValueError("La orientación debe ser 'horizontal' o 'vertical'.")

    #     return matriz_mutada
    
    
    
    # ----------------------  nueva Clase Radiacion -----------------------------------
class Radiacion(Mutador):
    
    def __init__(self, matriz_adn, base_nitrogenada, intensidad_mutacion, direccion):
        super().__init__(matriz_adn, base_nitrogenada, intensidad_mutacion)
        self.direccion = direccion  # aca viene desde ejecutable la direccion vert u horiz


    def crear_mutante(self, posicion_inicial):
        fila, columna = posicion_inicial

        # convertir las filas de la matriza listas para poder modificarlas
        for i in range(len(self.matriz_adn)):
            self.matriz_adn[i] = list(self.matriz_adn[i])

        for _ in range(self.intensidad_mutacion):
            self.matriz_adn[fila][columna] = self.base_nitrogenada

            # Modificar según la dirección
            if self.direccion == "horizontal":
                columna += 1
                if columna >= len(self.matriz_adn[0]):
                    break  # Evitar desbordar la matriz horizontalmente
            elif self.direccion == "vertical":
                fila += 1
                if fila >= len(self.matriz_adn):
                    break  # Evitar desbordar la matriz verticalmente

        # Convertir las filas de nuevo a strings si es necesario
        for i in range(len(self.matriz_adn)):
            self.matriz_adn[i] = ''.join(self.matriz_adn[i])

        return self.matriz_adn

    
    
    
#----------------------------------- nueva clase radiacion --------------------------------------




#----------------------------------- virus --------------------------------------
class Virus(Mutador):
    def __init__(self, matriz_adn, base_nitrogenada, intensidad_mutacion):
        # convertir las filas de la matriza listas para poder modificarlas
        self.matriz_adn = [list(fila) for fila in matriz_adn]
        super().__init__(self.matriz_adn, base_nitrogenada, intensidad_mutacion)

    def crear_mutante(self, posicion_inicial):
        fila, columna = posicion_inicial
        
        # aplicar la mutacion en la diagonal principal
        for i in range(self.intensidad_mutacion):
            if 0 <= fila + i < len(self.matriz_adn) and 0 <= columna + i < len(self.matriz_adn[0]):
                self.matriz_adn[fila + i][columna + i] = self.base_nitrogenada
        return self.matriz_adn




#----------------------------------- virus --------------------------------------



class Sanador(Detector):
    def __init__(self, adn, mutada):
        self.adn = adn
        self.mutada = mutada

    def sanar_mutacion(self, adn):
        
        # Usar solo las letras A, T, C, G  
        nuevas_letras = ['A', 'T', 'C', 'G']  
        
        # Reemplazar cada letra por una nueva letra aleatoria  
        for i in range(len(adn)):  
            adn[i] = ''.join(random.choice(nuevas_letras) for _ in range(len(adn[i])))  

        #Detectar si el adn sano no tiene mutaciones
        while Detector.detectar_diagonal_ascendente(self, adn) or Detector.detectar_diagonal_ascendente(self, adn) or Detector.detectar_horizontal(self, adn) or Detector.detectar_vertical(self, adn):
            for i in range(len(adn)):  
                adn[i] = ''.join(random.choice(nuevas_letras) for _ in range(len(adn[i]))) 

        self.mutada = False  
        return adn  
