from flask import Blueprint
# from controllers.auth_controller import unified_login, register_company, register_user
from controllers.company_user import add_user, delete_user, update_user, get_company_users

from middlewares.auth import token_required, company_required

user_bp = Blueprint('company', __name__)

# Company user management routes
user_bp.route('/add_user', methods=['POST'])(company_required(add_user))
user_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])(company_required(delete_user))
user_bp.route('/update_user/<int:user_id>', methods=['PUT'])(company_required(update_user))
user_bp.route('/users', methods=['GET'])(company_required(get_company_users))
