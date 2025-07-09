import requests

def login_usuario():
    print("\n=== Inicio de Sesión ===")
    correo = input("Correo: ")
    clave = input("Contraseña: ")

    datos = {
        "correo": correo,
        "clave": clave
    }

    try:
        response = requests.post("http://localhost:5000/login", json=datos)
        
        if response.status_code == 200:
            user = response.json()
            print(f"\n✅ Bienvenido {user['correo']} - Rol: {user['rol']}")
            # Aquí puedes continuar con el menú de personaje si es jugador.
            # Por ejemplo: mostrar_menu_personaje(user['correo'])

        else:
            print("❌ Error:", response.json().get("error"))

    except Exception as e:
        print("❌ No se pudo conectar al servidor:", e)
