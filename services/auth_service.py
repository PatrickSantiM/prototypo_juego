from config.database import get_db

def autenticar_usuario(correo, clave):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT u.id_user, u.correo, r.nombre_rol
        FROM usuario u
        JOIN rol r ON u.id_rol = r.id_rol
        WHERE u.correo = %s AND u.clave = %s
    """
    cursor.execute(query, (correo, clave))
    return cursor.fetchone()


def registrar_usuario(correo, clave):
    # Validaciones básicas
    if not correo.strip() or not clave.strip():
        print("❌ El correo y la contraseña no pueden estar vacíos.")
        return False

    if "@" not in correo:
        print("❌ El correo debe contener '@'.")
        return False

    if len(clave) < 6:
        print("❌ La contraseña debe tener al menos 6 caracteres.")
        return False

    conn = get_db()
    cursor = conn.cursor()

    # Verifica si el usuario ya existe
    cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
    if cursor.fetchone():
        print("❌ El correo ya está registrado.")
        return False

    # Registra usuario con rol 2 (Jugador)
    id_rol_jugador = 2
    query = "INSERT INTO usuario (correo, clave, id_rol) VALUES (%s, %s, %s)"
    cursor.execute(query, (correo, clave, id_rol_jugador))
    conn.commit()
    print("✅ Usuario registrado exitosamente.")
    return True

