from flask import Blueprint
from controllers.process_order import process_order

api = Blueprint('api', __name__)

api.route('/process-order', methods=['POST'])(process_order)