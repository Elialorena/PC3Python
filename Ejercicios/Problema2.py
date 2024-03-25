def obtener_calificaciones():
    while True:
        calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones = calificaciones_str.split(',')
        calificaciones_enteros = []
        for calificacion in calificaciones:
            try:
                calificacion_entero = int(calificacion)
                calificaciones_enteros.append(calificacion_entero)
            except ValueError:
                print("Error: Por favor, asegúrese de ingresar solo números enteros separados por comas.")
                return None
        return calificaciones_enteros

def main():
    calificaciones = obtener_calificaciones()
    if calificaciones is not None:
        print("Calificaciones ingresadas:", calificaciones)

if __name__ == "__main__":
    main()
