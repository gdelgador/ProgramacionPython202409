#ejercicio 5 de flujo control
salario=float(input("Ingrese su salario anual"))
tasa=0

if salario<=10000:
    tasa=5
elif salario>10000 and salario<=20000:
    tasa=10
elif salario>20000 and salario<=40000:
    tasa=12
else:
    tasa=15

impuesto=salario*tasa/100

print(f"el impuesto a pagar es {impuesto}")