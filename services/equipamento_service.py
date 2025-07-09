from config.database import get_db

def mostrar_equipamento_disponible():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipamento")
    equipamentos = cursor.fetchall()

    print("\n=== Lista de equipamento Disponible ===")
    for eq in equipamentos:
        print(f"[{eq['id_equipamento']}] {eq['name_equipamento']} - Tipo: {eq['tipo_equipamento']}")
        print(f"    Daño: {eq['daño_equipamento']} | Vida: {eq['vida_equipamento']}")
        print(f"    Descripción: {eq['descripcion_equipamento']}\n")

def obtener_equipamentos():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipamento")
    return cursor.fetchall()


def asignar_equipamiento_a_personaje(id_pj, id_equipamento):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO item_pj (id_pj, id_equipamento)
            VALUES (%s, %s)
        """, (id_pj, id_equipamento))
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error al asignar el equipamento: {e}")
        return False

def obtener_equipamiento_de_personaje(id_pj):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT e.name_equipamento, e.tipo_equipamento, e.descripcion_equipamento
        FROM equipamento e
        JOIN item_pj ip ON e.id_equipamento = ip.id_equipamento
        WHERE ip.id_pj = %s
    """
    cursor.execute(query, (id_pj,))
    return cursor.fetchall()
