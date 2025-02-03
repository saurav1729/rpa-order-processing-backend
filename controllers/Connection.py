from flask import jsonify, request
from models.Connection import Connection
from utils.db import db
import requests

def get_Connections():
    Connections = Connection.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": sub.id, "name": sub.name, "email": sub.email} for sub in Connections]), 200

def add_Connection(current_company):
    print("inside add_Connection")
    data = request.get_json()
    data['company_id'] = current_company.id  # Use current_company.id to associate with the company
    oauth_token = data.get('oauth_token')
    print(data['company_id'])

    # Check for missing fields
    if not all([oauth_token]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Use the oauth_token to fetch user info
    user_info = get_user_info_from_oauth(oauth_token)
    
    if not user_info:
        return jsonify({"error": "Invalid OAuth token or unable to fetch user info"}), 400

    name = user_info.get('email')
    email = user_info.get('email')

    # Check if name and email are available
    if not all([name, email]):
        return jsonify({"error": "Missing user info"}), 400
    
    # Create new Connection entry
    # Create new Connection entry
    new_Connection = Connection(name=name, oauth_token=oauth_token, company_id=current_company.id)
    
    # Add the new Connection to the database
    db.session.add(new_Connection)
    db.session.commit()
    
    return jsonify({"message": "Connection created!", "id": new_Connection.id}), 201

    print("inside add_Connection")
    data = request.get_json()
    data['company_id'] = current_company.id
    oauth_token = data.get('oauth_token')
    print(data['company_id'])

    # Check for missing fields
    if not all([oauth_token]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Use the oauth_token to fetch user info
    user_info = get_user_info_from_oauth(oauth_token)
    print(user_info)
    
    if not user_info:
        return jsonify({"error": "Invalid OAuth token or unable to fetch user info"}), 400

    name = user_info.get('name')
    email = user_info.get('email')

    # Check if name and email are available
    if not all([name, email]):
        return jsonify({"error": "Missing user info"}), 400
    
    # Create new Connection entry
    new_Connection = Connection(name=name, email=email, oauth_token=oauth_token, company_id=current_company.id)
    
    # Add the new Connection to the database
    db.session.add(new_Connection)
    db.session.commit()
    
    return jsonify({"message": "Connection created!", "id": new_Connection.id}), 201


def get_user_info_from_oauth(oauth_token):
    # Assuming OAuth provider API URL is 'https://api.oauthprovider.com/userinfo'
    headers = {"Authorization": f"Bearer {oauth_token}"}
    response = requests.get("https://www.googleapis.com/oauth2/v2/userinfo", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


def delete_Connection(id):
    Connection = Connection.query.filter_by(id=id, user_id=user_id).first()
    if Connection:
        db.session.delete(Connection)
        db.session.commit()
        return jsonify({"message": "Connection deleted"}), 200
    return jsonify({"error": "Connection not found"}), 404

def update_Connection(id):
    Connection = Connection.query.filter_by(id=id, user_id=user_id).first()
    if not Connection:
        return jsonify({"error": "Connection not found"}), 404
    
    data = request.json
    Connection.name = data.get('name', Connection.name)
    Connection.email = data.get('email', Connection.email)
    Connection.oauth_token = data.get('oauth_token', Connection.oauth_token)
    
    db.session.commit()
    return jsonify({"message": "Connection updated", "id": Connection.id}), 200

