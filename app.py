from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL (RDS)
db_config = {
    'host': 'paginaprueba.c1arstmsx1pg.us-east-1.rds.amazonaws.com',
    'user': 'admin',  # tu usuario RDS
    'password': 'Yancarlos12331#',  # tu contraseña RDS
    'database': 'paginaweb'  # cambia esto al nombre real de tu base de datos
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    nombre = request.form.get('input1')
    correo = request.form.get('input2')
    mensaje = request.form.get('input3')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO contacto (nombre, correo, mensaje) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, correo, mensaje))
        conn.commit()
        cursor.close()
        conn.close()
        return f"¡Datos guardados con éxito! Nombre: {nombre}, Correo: {correo}"
    except Exception as e:
        return f"Error al guardar en base de datos: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
