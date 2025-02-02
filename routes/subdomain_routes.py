from flask import Blueprint
from controllers.subdomain import add_subdomain ,Subdomain,delete_subdomain,update_subdomain
from middlewares.auth import token_required, company_or_admin_required

subdomain_bp = Blueprint('subdomain_routes', __name__)

subdomain_bp.route('/subdomains', methods=['GET'])(company_or_admin_required(Subdomain))

subdomain_bp.route('/addSubdomain', methods=['POST'])(company_or_admin_required(add_subdomain))

subdomain_bp.route('/subdomains/<int:id>', methods=['DELETE'])(company_or_admin_required(delete_subdomain))

subdomain_bp.route('/subdomains/<int:id>', methods=['PUT'])(update_subdomain)


