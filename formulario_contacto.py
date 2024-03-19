from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    # Correo al que se enviarán los datos
    destinatario = 'zubimendi@adminempresarial.onmicrosoft.com'  # Reemplaza esto con tu dirección de correo electrónico

    # Asunto del correo
    asunto = 'Nuevo mensaje de contacto'

    # Construir el cuerpo del correo
    cuerpo_correo = f"""
    Nombre: {nombre}
    Email: {email}
    Mensaje:
    {mensaje}
    """

    # Configurar el servidor SMTP
    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()
    # Aquí debes ingresar tus credenciales de correo electrónico
    correo_emisor = 'tu_correo@gmail.com'  # Reemplaza con tu correo electrónico
    contrasena = 'tu_contrasena'  # Reemplaza con tu contraseña

    # Iniciar sesión en el servidor SMTP
    servidor_smtp.login(correo_emisor, contrasena)

    # Construir el mensaje de correo
    mensaje_correo = MIMEMultipart()
    mensaje_correo['From'] = correo_emisor
    mensaje_correo['To'] = destinatario
    mensaje_correo['Subject'] = asunto
    mensaje_correo.attach(MIMEText(cuerpo_correo, 'plain'))

    # Enviar el correo
    servidor_smtp.sendmail(correo_emisor, destinatario, mensaje_correo.as_string())

    # Cerrar la conexión con el servidor SMTP
    servidor_smtp.quit()

    return '¡Gracias! Tu mensaje ha sido enviado.'

if __name__ == '__main__':
    app.run(debug=True)
