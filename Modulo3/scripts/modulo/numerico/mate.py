def calcular_factorial_recursivo(n:int)->int:
    """Calculo del factorial de un número de forma recursiva"""
    if n==1:
        return 1
    return n * calcular_factorial_recursivo(n-1)


def genera_listado_divisores(num):
    """Genera un listado de los divisores de un número"""

    # obtengo divisores
    listado_divisores = []
    for i in range(num):
        div = i+1

        if num % div == 0:
            listado_divisores.append(div)
        
    # retorno el listado de los numero
    return listado_divisores


def sumar_divisores_numero(num):
    """Retorna la suma de los divisores de un número"""
    return sum(genera_listado_divisores(num))


if __name__ == '__main__':
    print(calcular_factorial_recursivo(5))