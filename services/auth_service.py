from config.database import get_db

def autenticar_usuario(correo, clave):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT u.correo, r.nombre_rol
        FROM usuario u
        JOIN rol r ON u.id_rol = r.id_rol
        WHERE u.correo = %s AND u.clave = %s
    """
    cursor.execute(query, (correo, clave))
    return cursor.fetchone()


def registrar_usuario(correo, clave):
    conn = get_db()
    cursor = conn.cursor()

    # Verifica si el usuario ya existe
    cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
    if cursor.fetchone():
        return False

    # Registra usuario con rol 2 (Jugador)
    id_rol_jugador = 2
    query = "INSERT INTO usuario (correo, clave, id_rol) VALUES (%s, %s, %s)"
    cursor.execute(query, (correo, clave, id_rol_jugador))
    conn.commit()
    return True
