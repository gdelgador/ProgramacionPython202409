# Configuración del servidor y credenciales
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication



def enviar_correo(sender_email, sender_password, receiver_email, subject, body, file_path=None):
    """Funcion que permite enviar un correo y adjuntar un archivo si se desea"""

    # Configuración del servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crear el objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # adjuntar archivo
    if file_path:
        with open(file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype="csv")
            attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
            msg.attach(attachment)

    # Establecer conexión con el servidor SMTP, y envio correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Iniciar el modo seguro
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print('Correo enviado exitosamente')
 


if __name__ == '__main__':
    # Detalles del correo electrónico
    sender_email = 'gon2794@gmail.com'
    sender_password = open('/workspaces/ProgramacionPython202407/Modulo5/token.txt').read().strip()

    receiver_email = 'gonzalo.delgado.r@uni.pe'
    subject = 'Re-envio Reporte Vinos'
    body = 'Adjunto lo solicitado'
    file_path = '/workspaces/ProgramacionPython202407/Modulo5/scripts/procesamiento/salida_argumento.csv'  # Cambia la ruta al archivo que quieras adjuntar

    enviar_correo(sender_email, sender_password, receiver_email, subject, body, file_path)
    pass


