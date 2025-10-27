
def validar_numeros(a, b):
    try:
        a = float(a)
        b = float(b)
        return a, b
    except ValueError:
        raise ValueError("Ambos valores deben ser numéricos")


def suma(a, b):
    a, b = validar_numeros(a, b)
    return a + b


def resta(a, b):
    a, b = validar_numeros(a, b)
    return a - b


def multiplicacion(a, b):
    a, b = validar_numeros(a, b)
    return a * b


def division(a, b):
    a, b = validar_numeros(a, b)
    if b == 0:
        raise ZeroDivisionError("Error: división por cero no permitida")
    return a / b
