def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."
    
    import operaciones

print(operaciones.suma(5, 3))
print(operaciones.resta(5, 3))
print(operaciones.producto(5, 3))
print(operaciones.division(5, 3))
print(operaciones.division(5, 0))
print(operaciones.suma(5, "tres"))