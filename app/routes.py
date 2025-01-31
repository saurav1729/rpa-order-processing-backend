from flask import Blueprint, request, jsonify
import json
from app.model import generate_response

api = Blueprint('api', __name__)

@api.route('/process-order', methods=['POST'])
def process_order():
    try:
        data = request.get_json()
        print("incoming request")
        print(data); 
        structured_json = generate_response(data)
        response = json.loads(structured_json)
        print("response generated:")
        print(response)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
