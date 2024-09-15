# funcion apartir de python 3.10
menu="""
    Bienvenidos a Python Datux
    1.Sumar Numeros
    2.Restar Numeros
    3.Multiplicar
    4.Salir
"""
print(menu)
opcion= int(input("Elije tu opcion:"))

match opcion:
    case 1:
         numberOne=float(input("ingrese numero 1: "))
         numberTwo=float(input("ingrese numero 2: "))
         resultado=numberOne+numberTwo
         print(f"La suma es {resultado}")
    case 2:
         numberOne=float(input("ingrese numero 1: "))
         numberTwo=float(input("ingrese numero 2: "))
         resultado=numberOne-numberTwo
         print(f"La resta es {resultado}")
### ... replicar otras opciones
    case _:
          print("Opcion no valida ")