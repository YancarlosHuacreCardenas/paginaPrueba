# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

# Ruta principal que podría servir tu archivo HTML (si estuviera en la carpeta 'templates')
@app.route('/')
def index():
    # En un escenario real, aquí podrías renderizar tu archivo HTML
    # Por ejemplo: return render_template('index.html')
    # Para este ejercicio, solo devolvemos un mensaje.
    return "¡Hola desde el servidor Flask! Si ves esto, el servidor está funcionando."

# Ruta para manejar el envío del formulario (si el formulario lo enviara aquí)
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Aquí es donde recibirías los datos del formulario
        # Por ejemplo, si tus campos se llamaran 'input1', 'input2', 'input3'
        nombre = request.form.get('input1')
        correo = request.form.get('input2')
        mensaje = request.form.get('input3')

        print(f"Datos recibidos del formulario:")
        print(f"Nombre: {nombre}")
        print(f"Correo: {correo}")
        print(f"Mensaje: {mensaje}")

        # Aquí podrías guardar los datos en una base de datos, enviar un correo, etc.

        # Devolvemos una respuesta al cliente
        return f"¡Datos recibidos con éxito! Nombre: {nombre}, Correo: {correo}"
    return "Método no permitido", 405 # Si alguien intenta acceder con GET

if __name__ == '__main__':
    # Para ejecutar esta aplicación:
    # 1. Guarda este código como app.py
    # 2. Abre tu terminal en la misma carpeta
    # 3. Instala Flask: pip install Flask
    # 4. Ejecuta: python app.py
    # 5. La aplicación estará disponible en http://127.0.0.1:5000/
    app.run(debug=True) # debug=True permite recarga automática y mensajes de error
