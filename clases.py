class Detector:
    def __init__(self,adn_lng,mutacion,adn):
        self.adn_lng = adn_lng,
        self.mutacion = mutacion,
        self.adn = adn,
    def detectar_mutantes_vertical(self):
        n = self.adn_lng
        matriz_adn = self.adn
        for i in range(n):
            for j in range(n -self.secuencia + 1):
                if([matriz_adn[i + k][j] for k in range(self.secuencia)]) :
                    self.mutacion = True
                    return self.mutacion
    def detectar_mutantes_horizontal(self):
        n = self.adn_lng
        matriz_adn = self.adn
        if ([matriz_adn[i][j+k] for k in range(self.secuencia)]):
            self.mutacion = True
            return self.mutacion
    def detectar_mutantes_diagonal(self):
        pass
    pass

class Mutador:
    pass

class Radiacion(Mutador):
    pass

class Virus(Mutador):
    pass

class Sanador:
    pass
