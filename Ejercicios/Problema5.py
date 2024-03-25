class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del alumno:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.num_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No especificadas")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas


