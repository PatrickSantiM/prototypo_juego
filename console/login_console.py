import sys
import os
from services.auth_service import autenticar_usuario
from console.menu_personajes import menu_personajes
from console.menu_gm import menu_gm

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_usuario():
    limpiar_pantalla()
    print("\n=== Inicio de Sesión ===")
    correo = input("Correo: ")
    clave = input("Contraseña: ")

    usuario = autenticar_usuario(correo, clave)

    if usuario:
        print(f"\n✅ Bienvenido {usuario['correo']} - Rol: {usuario['nombre_rol']}")
        if usuario['nombre_rol'].lower() == "jugador":
            print("🔓 Accediendo al menú de personajes...")
            menu_personajes(usuario['id_user'])  # <-- Aquí le pasas el ID
        elif usuario['nombre_rol'].lower() == "gm":
            print("🎮 Accediendo al panel de Game Master...")
            menu_gm(usuario['id_user'])
    else:
        print("❌ Correo o contraseña incorrectos.")
