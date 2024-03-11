<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página con Flask</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f2f2f2; /* Cambia este valor a tu tono de gris preferido */
        }
        header {
            text-align: center;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
        }
        main {
            margin-block-start: 20px;
        }
        footer {
            text-align: center;
            padding: 10px;
            position: fixed;
            inset-block-end: 0; /* Corrige el error tipográfico aquí */
            inline-size: 100%;
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>

    <header>
        <h1>Mi Página con Flask</h1>
    </header>

    <main>
        <h2>¡Bienvenido, {{ nombre }}!</h2>
        <p>Esta es una página HTML servida por Flask, un framework de Python para desarrollo web. Visita algunas secciones interesantes:</p>
        
        <ul>
            {% for enlace in enlaces %}
                <li><a href="{{ enlace['url'] }}">{{ enlace['nombre'] }}</a></li>
            {% endfor %}
        </ul>
    </main>

    <footer>
        <p>&copy; 2024 Mi Página con Flask. Todos los derechos reservados.</p>
    </footer>

</body>
</html>
