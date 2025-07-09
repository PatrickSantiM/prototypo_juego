from flask import Blueprint
from controllers.auth_controller import login_jugador, registrar_jugador

auth_bp = Blueprint('auth_bp', __name__)


auth_bp.route('/login', methods=['POST'])(login_jugador)
auth_bp.route('/register', methods=['POST'])(registrar_jugador)
