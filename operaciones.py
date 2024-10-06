def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")


def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")


def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")


def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        return a / b
    except TypeError:
        print("Error: Tipo de dato no válido.")
    except ZeroDivisionError as e:
        print(e)
