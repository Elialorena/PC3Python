class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    @property
    def calcular_area(self):
        return self.largo * self.ancho