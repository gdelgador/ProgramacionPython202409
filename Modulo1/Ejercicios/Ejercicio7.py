datux_python={
    "HORARIO":"9-13",
    "FRECUENCIA":"DOMINGOS",
    "PROFESORES":["PX1","PX2","PX3"],
    "ALUMNOS":[
        {
            "NOMBRE":"DARIO",
            "ESPECIALIDAD":"INGENIERA",
            "NOTAS":[12,15,16,12]
        },
    ]
}
print(datux_python)
# PROGRAMA QUE AGREGUE ALUMNOS
nombre=input("Ingrese su nombre")
especialidad=input("Ingrese su especialidad")
have_notes=input("Tiene notas si/no")

if have_notes.lower()=='si':
    nota=int(input("Ingrese sus notas"))
    datux_python["ALUMNOS"].append(
        {
            "NOMBRE":nombre,
            "ESPECIALIDAD":especialidad,
            "NOTAS":[nota]
        }
    )
else:
    datux_python["ALUMNOS"].append(
        {
            "NOMBRE":nombre,
            "ESPECIALIDAD":especialidad,
            "NOTAS":[]
        }
    )

print(datux_python)