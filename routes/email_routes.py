# from flask import Blueprint, request, jsonify
# # from models.email_config import EmailConfig
# from services.email_service import process_email
# from utils.db import db
# # from app import db

# email_bp = Blueprint('email_routes', __name__)

# @email_bp.route('/email/configure', methods=['POST'])
# def configure_email():
#     data = request.json
#     email_config = EmailConfig(
#         email=data['email'],
#         order_url=data['order_url'],
#         method=data['method'],
#         headers=data['headers'],
#         origin_folder=data['origin_folder'],
#         destination_folder=data['destination_folder'],
#         error_folder=data['error_folder']
#     )
#     db.session.add(email_config)
#     db.session.commit()
#     return jsonify({"message": "Email configured successfully"}), 201

# # @email_bp.route('/email/process', methods=['POST'])
# # def process_email():
# #     data = request.json
# #     result = process_email(data['email'])
# #     # Process email logic here (call external API, filter, etc.)
# #     return jsonify({"message": "Email processed", data:result}), 200
