import requests

def registrar_usuario():
    print("\n=== Registro de Usuario (Jugador) ===")
    correo = input("Ingrese su correo: ")
    clave = input("Ingrese su contraseña: ")

    datos = {
        "correo": correo,
        "clave": clave
    }

    try:
        response = requests.post("http://localhost:3306/register", json=datos)

        if response.status_code == 200:
            print("✅ Usuario registrado exitosamente.")
        elif response.status_code == 409:
            print("⚠️ Este correo ya está registrado.")
        else:
            print(f"❌ Error: {response.json().get('error')}")

    except Exception as e:
        print(f"❌ Error de conexión con el servidor: {e}")
