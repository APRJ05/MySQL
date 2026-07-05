from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def conectar():
    while True:
        try:
            conexion = mysql.connector.connect(
                host="db",
                user="root",
                password="123456",
                database="prueba"
            )
            return conexion
        except:
            print("Esperando MySQL...")
            time.sleep(3)

@app.route("/")
def inicio():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("SELECT 'Hola desde MySQL';")

    mensaje = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return f"<h1>{mensaje}</h1>"

app.run(host="0.0.0.0", port=5000)