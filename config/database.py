import mysql.connector
from mysql.connector import Error

def get_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="qwerty12345",
            database="juego"
        )
        return connection
    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None