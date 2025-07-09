from flask import request, jsonify
from services.auth_service import autenticar_usuario, registrar_usuario

def login_jugador():
    data = request.json
    correo = data.get('correo')
    clave = data.get('clave')

    if not correo or not clave:
        return jsonify({"error": "Debe ingresar correo y clave"}), 400

    usuario = autenticar_usuario(correo, clave)

    if not usuario:
        return jsonify({"error": "Credenciales inválidas"}), 401

    if usuario['nombre_rol'].upper() == 'GM':
        return jsonify({"error": "Los GM no pueden acceder desde este login"}), 403

    return jsonify({
        "mensaje": "Inicio de sesión exitoso",
        "correo": usuario['correo'],
        "rol": usuario['nombre_rol']
    })


def registrar_jugador():
    data = request.json
    correo = data.get('correo')
    clave = data.get('clave')

    if not correo or not clave:
        return jsonify({"error": "Debe ingresar correo y clave"}), 400

    if registrar_usuario(correo, clave):
        return jsonify({"mensaje": "Usuario registrado correctamente"})
    else:
        return jsonify({"error": "El correo ya está registrado"}), 409
