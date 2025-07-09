from config.database import get_db

def obtener_razas():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM raza")
    return cursor.fetchall()

def obtener_habilidades_por_raza(id_raza):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT h.name_habilidades, h.descripcion_habilidades, h.daño_habilidades
        FROM habilidades h
        JOIN habilidades_raza hr ON h.id_habilidades = hr.id_habilidades
        WHERE hr.id_raza = %s
    """
    cursor.execute(query, (id_raza,))
    return cursor.fetchall()

def obtener_poderes_por_raza(id_raza):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT p.name_poderes, p.descripcion_poderes, p.daño_poderes
        FROM poderes p
        JOIN poderes_raza pr ON p.id_poderes = pr.id_poderes
        WHERE pr.id_raza = %s
    """
    cursor.execute(query, (id_raza,))
    return cursor.fetchall()

def crear_personaje(nombre, id_usuario, id_raza):
    conn = get_db()
    cursor = conn.cursor()

    estado_inicial = 1
    nivel_inicial = 1

    query = """
        INSERT INTO personajes (name_pj, nivel_pj, id_user, id_raza, id_estado)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, (nombre, nivel_inicial, id_usuario, id_raza, estado_inicial))
        conn.commit()
        return cursor.lastrowid  # Retorna el ID del personaje
    except Exception as e:
        print("Error al insertar personaje:", e)
        return None
    
def actualizar_personaje(id_pj, nuevo_nombre=None, nuevo_nivel=None, nuevo_estado=None):
    conn = get_db()
    cursor = conn.cursor()
    campos = []
    valores = []

    if nuevo_nombre:
        campos.append("name_pj = %s")
        valores.append(nuevo_nombre)
    if nuevo_nivel:
        campos.append("nivel_pj = %s")
        valores.append(nuevo_nivel)
    if nuevo_estado:
        campos.append("id_estado = %s")
        valores.append(nuevo_estado)

    if not campos:
        return False

    valores.append(id_pj)
    query = f"UPDATE personajes SET {', '.join(campos)} WHERE id_pj = %s"
    cursor.execute(query, tuple(valores))
    conn.commit()
    return cursor.rowcount > 0


def obtener_personajes_por_usuario(id_usuario):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT pj.id_pj, pj.name_pj, pj.nivel_pj, pj.id_raza, r.name_raza, e.tipo_estado
        FROM personajes pj
        JOIN raza r ON pj.id_raza = r.id_raza
        JOIN estado e ON pj.id_estado = e.id_estado
        WHERE pj.id_user = %s
    """
    cursor.execute(query, (id_usuario,))
    return cursor.fetchall()

def obtener_todos_los_personajes():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT p.id_pj, p.name_pj, p.nivel_pj, u.correo, r.name_raza, e.tipo_estado
        FROM personajes p
        JOIN usuario u ON p.id_user = u.id_user
        JOIN raza r ON p.id_raza = r.id_raza
        JOIN estado e ON p.id_estado = e.id_estado
    """
    cursor.execute(query)
    return cursor.fetchall()

