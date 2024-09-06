
PI_CONSTANT = 3.1416


def ingreso_numero_entero(msg='Ingrese un número entero: '):
    """Función que solicita un número entero al usuario"""
    try:
        numero = int(input(msg))
        return numero
    except ValueError:
        print('Por favor, ingrese un número entero válido ...')
        return ingreso_numero_entero(msg)
    

def ingreso_numero_decimal(msg='Ingrese un número decimal: '):
    """Función que solicita un número entero al usuario"""
    try:
        numero = float(input(msg))
        return numero
    except ValueError:
        print('Por favor, ingrese un número decimal válido ...')
        return ingreso_numero_decimal(msg)
    