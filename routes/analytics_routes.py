# from flask import Blueprint, jsonify
# from models.analytics import Analytics

# analytics_bp = Blueprint('analytics', __name__)

# @analytics_bp.route('/analytics', methods=['GET'])
# def get_analytics():
#     data = {
#         "order_failed": 10,
#         "order_passed": 50,
#         "mail_failed": 5,
#         "mail_passed": 80,
#         "downtime": "2 hours",
#         "peak_time": "3 PM - 5 PM"
#     }
#     return jsonify(data)
