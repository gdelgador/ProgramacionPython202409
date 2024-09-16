menu="""
    Bienvenidos a Python Datux
    1.Sumar Numeros
    2.Restar Numeros
    3.Multiplicar
    4.Salir
"""
print(menu)
opcion= int(input("Elije tu opcion:"))

if opcion ==1:
    numberOne=float(input("ingrese numero 1: "))
    numberTwo=float(input("ingrese numero 2: "))
    resultado=numberOne+numberTwo
    print(f"La suma es {resultado}")
elif opcion ==2:
    numberOne=float(input("ingrese numero 1: "))
    numberTwo=float(input("ingrese numero 2: "))
    resultado=numberOne-numberTwo
    print(f"La resta es {resultado}")
elif opcion ==3:
    numberOne=float(input("ingrese numero 1: "))
    numberTwo=float(input("ingrese numero 2: "))
    resultado=numberOne*numberTwo
    print(f"La multiplicacion es {resultado}")
elif opcion ==4:
    print("Hasta luego")
else:
    print("Opcion no valida")


