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
#Mutaqdor

class Mutador:
    def __init__(self, base_nitrogenada, coordenadas=[]):
        try:
            # validamos que las bases nitrogenadas sean una opcion corrects A T C o G
            if base_nitrogenada not in {'A', 'T', 'C', 'G'}:
                raise ValueError("La base nitrogenada debe ser una de las siguientes: 'A', 'T', 'C', 'G'.")
            self.base_nitrogenada = base_nitrogenada

            # validamos que las coordenadas esten detnro de la matriz de 6x6, osea los valores de 0 a 5
            for coord in coordenadas:
                if not (0 <= coord[0] < 6 and 0 <= coord[1] < 6):
                    raise ValueError("Las coordenadas deben estar dentro de los límites de la matriz (0 a 5).")
            self.coordenadas = coordenadas
            
            # estado de la mutazion, lo dejamos como un booleano que nos puede servir para mostrar un mensaje si la matriz fue mutada
            self.mutacion_realizada = False

        except ValueError as e:
            print(f"Error al inicializar Mutador: {e}")
    
    # el metodo esta vacio para ser implementado en una subclase (radiacion o virus)
    def crear_mutante(self):
        pass  


#--------------------------------------------------------------------------------------------------------



class Radiacion(Mutador):
    pass

class Virus(Mutador):
    pass

class Sanador(Detector):
    def __init__(self, adn, mutada):
        super().__init__(adn)
        self.mutada = mutada

    def sanar_mutacion(self, adn):
        
         # Usar solo las letras A, T, C, G  
        nuevas_letras = ['A', 'T', 'C', 'G']  
        
        # Reemplazar cada letra por una nueva letra aleatoria  
        if Detector.detectar_diagonal_ascendente(self, adn) or Detector.detectar_diagonal_ascendente(self, adn) or Detector.detectar_horizontal(self, adn) or Detector.detectar_vertical(self, adn):
            for i in range(len(adn)):  
                adn[i] = ''.join(random.choice(nuevas_letras) for _ in range(len(adn[i])))  

            #Detectar si el adn sano no tiene mutaciones
            while Detector.detectar_diagonal_ascendente(self, adn) or Detector.detectar_diagonal_ascendente(self, adn) or Detector.detectar_horizontal(self, adn) or Detector.detectar_vertical(self, adn):
                for i in range(len(adn)):  
                    adn[i] = ''.join(random.choice(nuevas_letras) for _ in range(len(adn[i]))) 
            
            print(f"Adn sano: {adn}")
        else:
            print(">> SU ADN YA ESTÁ SANO <<")

        self.mutada = False  
        return adn  