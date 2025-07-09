import os
import time
from services.equipamento_service import obtener_equipamentos, asignar_equipamiento_a_personaje, obtener_equipamiento_de_personaje
from services.personaje_service import (
    crear_personaje,
    obtener_razas,
    obtener_habilidades_por_raza,
    obtener_poderes_por_raza,
    obtener_personajes_por_usuario
)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_personajes(id_usuario):
    personajes = obtener_personajes_por_usuario(id_usuario)
    if not personajes:
        print("⚠️ No tienes personajes aún.")
        input("\nPresiona Enter para continuar...")
        return

    print("\n=== TUS PERSONAJES ===")
    for idx, pj in enumerate(personajes, 1):
        print(f"{idx}. {pj['name_pj']} | Nivel: {pj['nivel_pj']} | Raza: {pj['name_raza']} | Estado: {pj['tipo_estado']}")

    try:
        opcion = input("\n¿Deseas ver detalles de un personaje? (s/n): ")
        if opcion.lower() == 's':
            seleccion = int(input("Selecciona el número del personaje: "))
            if 1 <= seleccion <= len(personajes):
                pj = personajes[seleccion - 1]
                mostrar_detalle_personaje(pj)
            else:
                print("❌ Selección inválida.")
    except ValueError:
        print("❌ Entrada inválida.")

    input("\nPresiona Enter para continuar...")

def mostrar_detalle_personaje(pj):
    print(f"\n📋 Detalles de {pj['name_pj']}")
    print(f"Nivel: {pj['nivel_pj']}")
    print(f"Raza: {pj['name_raza']}")
    print(f"Estado: {pj['tipo_estado']}")

    equipo = obtener_equipamiento_de_personaje(pj['id_pj'])

    print("\n🛡️ Equipamiento:")
    if equipo:
        for eq in equipo:
            print(f"- {eq['name_equipamento']} ({eq['tipo_equipamento']}): {eq['descripcion_equipamento']}")
    else:
        print("Sin equipamiento asignado.")

    habilidades = obtener_habilidades_por_raza(pj['id_raza'])
    poderes = obtener_poderes_por_raza(pj['id_raza'])

    print("\n🧬 Habilidades:")
    for hab in habilidades:
        print(f"- {hab['name_habilidades']}: {hab['descripcion_habilidades']} (Daño: {hab['daño_habilidades']})")

    print("\n🔮 Poderes:")
    for pod in poderes:
        print(f"- {pod['name_poderes']}: {pod['descripcion_poderes']} (Daño: {pod['daño_poderes']})")


def asignar_equipamiento_menu(id_personaje):
    print("=== SELECCIÓN DE EQUIPAMIENTO INICIAL ===")

    equipamentos = obtener_equipamentos()
    if not equipamentos:
        print("⚠️ No hay equipamientos disponibles.")
        return

    for idx, eq in enumerate(equipamentos, 1):
        print(f"{idx}. {eq['name_equipamento']} - {eq['descripcion_equipamento']}")

    try:
        seleccion = int(input("\nSeleccione un equipamiento (número): "))
        if seleccion < 1 or seleccion > len(equipamentos):
            raise ValueError

        equipo_seleccionado = equipamentos[seleccion - 1]

        confirmacion = input(f"\n¿Asignar '{equipo_seleccionado['name_equipamento']}' al personaje? (s/n): ")
        if confirmacion.lower() == 's':
            exito = asignar_equipamiento_a_personaje(id_personaje, equipo_seleccionado['id_equipamento'])
            if exito:
                print("✅ Equipamiento asignado correctamente.")
            else:
                print("❌ Error al asignar el equipamiento.")
        else:
            print("❌ Asignación cancelada.")
    except ValueError:
        print("❌ Selección inválida.")

    input("\nPresiona Enter para continuar...")

def crear_personaje_menu(id_usuario):
    limpiar_pantalla()
    print("=== CREAR NUEVO PERSONAJE ===")

    razas = obtener_razas()
    if not razas:
        print("❌ No hay razas disponibles.")
        return

    print("\n--- Razas Disponibles ---")
    for idx, raza in enumerate(razas, 1):
        print(f"{idx}. {raza['name_raza']} - {raza['descripcion_raza']} (❤️ {raza['vida_raza']} / ⚔️ {raza['daño_raza']})")

    try:
        seleccion = int(input("\nSeleccione una raza (número): "))
        if seleccion < 1 or seleccion > len(razas):
            raise ValueError

        raza_elegida = razas[seleccion - 1]
        id_raza = raza_elegida['id_raza']

        habilidades = obtener_habilidades_por_raza(id_raza)
        poderes = obtener_poderes_por_raza(id_raza)

        print(f"\n🧬 Habilidades de {raza_elegida['name_raza']}:")
        for hab in habilidades:
            print(f"- {hab['name_habilidades']}: {hab['descripcion_habilidades']} (Daño: {hab['daño_habilidades']})")

        print(f"\n🔮 Poderes de {raza_elegida['name_raza']}:")
        for pod in poderes:
            print(f"- {pod['name_poderes']}: {pod['descripcion_poderes']} (Daño: {pod['daño_poderes']})")

        nombre_pj = input("\nIngrese nombre del personaje: ")
        confirmacion = input(f"¿Crear personaje '{nombre_pj}' como raza '{raza_elegida['name_raza']}'? (s/n): ")

        if confirmacion.lower() == 's':
            id_pj = crear_personaje(nombre_pj, id_usuario, id_raza)
            if id_pj:
                print("✅ Personaje creado exitosamente.")
                asignar_equipamiento_menu(id_pj)
            else:
                print("❌ Error al crear el personaje.")
        else:
            print("❌ Creación cancelada.")

    except ValueError:
        print("❌ Selección inválida.")

    input("\nPresiona Enter para continuar...")

def menu_personajes(id_usuario):
    while True:
        limpiar_pantalla()
        print("=== MENÚ DE PERSONAJES ===")
        print("1. Ver Personajes")
        print("2. Crear Personaje")
        print("3. Volver al Menú Principal")
        opcion = input("\nSeleccione una opción (1-3): ")

        if opcion == "1":
            limpiar_pantalla()
            mostrar_personajes(id_usuario)
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            crear_personaje_menu(id_usuario)
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida.")
            input("\nPresiona Enter para continuar...")
