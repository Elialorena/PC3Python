def calcular_porcentaje(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if denominator == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        if numerator > denominator or numerator < 0:
            raise ValueError("La fracción debe ser mayor o igual a 0 y menor o igual al total.")
        percentage = (numerator / denominator) * 100
        if percentage < 1:
            return 'E'
        elif percentage > 99:
            return 'F'
        else:
            return str(round(percentage)) + '%'
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return None

def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        result = calcular_porcentaje(fraction)
        if result is not None:
            print("Cantidad de combustible en el tanque:", result)
            break

if __name__ == "__main__":
    main()
