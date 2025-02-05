from flask import Blueprint, Flask, request, jsonify, redirect, session
from controllers.Connection import add_Connection,delete_Connection,get_Connections
from middlewares.auth import token_required, company_or_admin_required



Connection_bp = Blueprint('Connection_routes', __name__)

# Correct route definitions
Connection_bp.route('/Connections', methods=['GET'])(company_or_admin_required(get_Connections))
Connection_bp.route('/addConnection', methods=['POST'])(company_or_admin_required(add_Connection))
Connection_bp.route('/Connections/<int:id>', methods=['DELETE'])(company_or_admin_required(delete_Connection))

