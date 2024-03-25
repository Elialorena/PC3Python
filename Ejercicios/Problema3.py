class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return round(3.14159 * self.radio ** 2, 2)  # Redondear el resultado a 2 decimales


