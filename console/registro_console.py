from services.auth_service import registrar_usuario

def registrar_usuario_menu():
    print("\n=== Registro de Usuario (Jugador) ===")
    correo = input("Ingrese su correo: ")
    clave = input("Ingrese su contraseña: ")

    registrado = registrar_usuario(correo, clave)

    if registrado:
        print("✅ Usuario registrado exitosamente.")
    else:
        print("⚠️ Este correo ya está registrado o hubo un error.")
