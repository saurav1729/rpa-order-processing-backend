from flask import jsonify, request
from models.Connection import Connection
from app.model import generate_response
from utils.db import db
import json

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