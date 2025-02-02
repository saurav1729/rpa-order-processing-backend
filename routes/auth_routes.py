from flask import Blueprint
from controllers.auth_controller import register_company, unified_login

auth_bp = Blueprint('auth_routes', __name__)

auth_bp.route('/register', methods=['POST'])(register_company)
auth_bp.route('/login', methods=['POST'])(unified_login)
