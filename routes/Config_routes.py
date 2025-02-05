from flask import Blueprint
from controllers.Configure_bot import configure_bot, update_bot, delete_bot
from middlewares.auth import company_or_admin_required

Config_bp = Blueprint('Config_routes', __name__)

# Route to configure a bot
Config_bp.route('/addBot', methods=['POST'])(company_or_admin_required(configure_bot))

# Route to update an existing bot configuration
Config_bp.route('/updateBot/<int:bot_id>', methods=['PUT'])(company_or_admin_required(update_bot))

# Route to delete a bot configuration
Config_bp.route('/deleteBot/<int:bot_id>', methods=['DELETE'])(company_or_admin_required(delete_bot))
