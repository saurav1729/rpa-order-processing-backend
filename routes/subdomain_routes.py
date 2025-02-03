from flask import Blueprint, Flask, request, jsonify, redirect, session
from controllers.subdomain import add_subdomain, delete_subdomain, update_subdomain ,get_subdomains
from middlewares.auth import token_required, company_or_admin_required


subdomain_bp = Blueprint('subdomain_routes', __name__)

# Correct route definitions
# subdomain_bp.route('/subdomains', methods=['GET'])(company_or_admin_required(get_subdomains))
subdomain_bp.route('/addSubdomain', methods=['POST'])(company_or_admin_required(add_subdomain))
subdomain_bp.route('/subdomains/<int:id>', methods=['DELETE'])(company_or_admin_required(delete_subdomain))
subdomain_bp.route('/subdomains/<int:id>', methods=['PUT'])(company_or_admin_required(update_subdomain))
