<?php
// Obtener los datos del formulario
$nombre = $_POST['nombre'];
$email = $_POST['email'];
$mensaje = $_POST['mensaje'];

// Correo al que se enviarán los datos
$destinatario = 'zubimendi@adminempresarial.onmicrosoft.com'; // Reemplaza esto con tu dirección de correo electrónico

// Asunto del correo
$asunto = 'Nuevo mensaje de contacto';

// Construir el cuerpo del correo
$mensaje_correo = "Nombre: $nombre\n";
$mensaje_correo .= "Email: $email\n";
$mensaje_correo .= "Mensaje:\n$mensaje\n";

// Cabeceras del correo
$cabeceras = "From: $nombre <$email>";

// Enviar el correo
if (mail($destinatario, $asunto, $mensaje_correo, $cabeceras)) {
    echo '¡Gracias! Tu mensaje ha sido enviado.';
} else {
    echo 'Hubo un error al enviar tu mensaje. Por favor, inténtalo de nuevo más tarde.';
}
?>
