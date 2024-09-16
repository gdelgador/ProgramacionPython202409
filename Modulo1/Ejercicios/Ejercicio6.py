#enviar mensaje wsp
codigo_bloqueo="123456"

codigo=input("ingrese su codigo de bloque de celular: ")
#contacto1="Juan carlos"
#contacto2="Gian"
#contacto3="Camila"
#contacto4="Efrain"
#refactor
lista_contacto=["juan carlos","gian","camila","efrain"]
# list(map(str.lower,lista_contacto)) => opcion avanzada
if codigo_bloqueo.lower()==codigo.lower():
    print("Ingreso correctamente")
    app=input("Ingrese la app a revisar:")
    print(f"el {app} abierto correctamente") 
    contacto_enviar=input("Ingrese el contacto a chatear: ")
    contacto_confirmado=True
    mensaje=""
    if contacto_enviar.lower() in lista_contacto:
        mensaje=input("Ingrese el mensaje: ")
    else:
        contacto_confirmado=False
        print("no tiene ese contacto")

    if contacto_confirmado:
        confirmacion=input("Desea enviar el mensaje:(si/no)")
        if 'SI'.upper() == confirmacion.upper():
            print("se envio el mensaje correctamente: ")
            print(f'{contacto_enviar} => {mensaje}')
        else:
            print("Gracias")

else:
    print("el codigo es incorrecto")