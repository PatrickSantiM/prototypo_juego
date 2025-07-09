import os
import time
from services.personaje_service import obtener_todos_los_personajes, actualizar_personaje


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ver_todos_los_personajes():
    personajes = obtener_todos_los_personajes()
    if not personajes:
        print("\n⚠️ No hay personajes registrados.")
        return

    print("\n=== LISTA DE TODOS LOS PERSONAJES ===")
    for pj in personajes:
        print(f"- {pj['name_pj']} | Nivel: {pj['nivel_pj']} | Usuario: {pj['correo']} | Raza: {pj['name_raza']} | Estado: {pj['tipo_estado']}")

def modificar_ficha_personaje():
    personajes = obtener_todos_los_personajes()
    if not personajes:
        print("⚠️ No hay personajes disponibles.")
        return

    print("\n=== PERSONAJES DISPONIBLES ===")
    for idx, pj in enumerate(personajes, 1):
        print(f"{idx}. {pj['name_pj']} - Nivel {pj['nivel_pj']} - Estado: {pj['tipo_estado']} - Raza: {pj['name_raza']}")

    try:
        seleccion = int(input("Seleccione el personaje a modificar (número): "))
        if seleccion < 1 or seleccion > len(personajes):
            raise ValueError
        personaje = personajes[seleccion - 1]

        print("\nDeja en blanco si no deseas modificar ese campo.")
        nuevo_nombre = input(f"Nuevo nombre [{personaje['name_pj']}]: ") or None
        nuevo_nivel = input(f"Nuevo nivel [{personaje['nivel_pj']}]: ")
        nuevo_estado = input("Nuevo ID de estado (ej: 1 = vivo, 2 = muerto): ")

        nuevo_nivel = int(nuevo_nivel) if nuevo_nivel else None
        nuevo_estado = int(nuevo_estado) if nuevo_estado else None

        actualizado = actualizar_personaje(personaje['id_pj'], nuevo_nombre, nuevo_nivel, nuevo_estado)
        if actualizado:
            print("✅ Personaje actualizado con éxito.")
        else:
            print("⚠️ No se realizaron cambios.")
    except ValueError:
        print("❌ Selección inválida.")


def menu_gm(id_usuario):
    while True:
        limpiar_pantalla()
        print("=== MENÚ DEL GAME MASTER ===")
        print("1. Ver todos los personajes")
        print("2. Modificar ficha de personaje")
        print("3. Agregar nuevas razas/habilidades/poderes/equipamientos")
        print("4. Editar habilidades y poderes por raza")
        print("5. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            limpiar_pantalla()
            ver_todos_los_personajes()
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            modificar_ficha_personaje()
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            print("🚧 Función en desarrollo: Agregar nuevas entidades")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            print("🚧 Función en desarrollo: Editar habilidades y poderes")
            input("\nPresiona Enter para continuar...")

        elif opcion == "5":
            break

        else:
            print("❌ Opción inválida.")
            input("\nPresiona Enter para continuar...")
