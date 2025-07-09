import os
import time
from registro_console import registrar_usuario
from login_console import login_usuario

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpiar_pantalla()
        print("=== MENÚ PRINCIPAL ===")
        print("1. Registrarse como Jugador")
        print("2. Iniciar Sesión (Jugador)")
        print("3. Salir")
        opcion = input("\nSeleccione una opción (1-3): ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            print("¡Hasta luego!")
            time.sleep(1)
            break
        else:
            print("❌ Opción inválida.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
