

def factorial_recursivo(numero):
    """Calcula el factorial de un número de forma recursiva"""
    assert numero >= 0, "Debes ingresar un número positivo"
    
    if numero == 0 or numero==1:
        return 1
    return numero * factorial_recursivo(numero-1)


# Probamos
if __name__ == '__main__':

    x = factorial_recursivo(5) # 120
    print(x)