from flask import jsonify, request
from models.Connection import Connection
from utils.db import db
import requests

def get_Connections(current_company):
    print(current_company.id)
    company_id = current_company.id
    Connections = Connection.query.filter_by(company_id=company_id).all()
    return jsonify([{"id": sub.id, "name": sub.name, "email": sub.email, "company_id":sub.company_id} for sub in Connections]), 200

def add_Connection(current_company):
    print("inside add_Connection")
    data = request.get_json()
    data['company_id'] = current_company.id  # Use current_company.id to associate with the company
    oauth_token = data.get('oauth_token')
    print("oauth token", oauth_token)
    print("company id", data['company_id'])

    # Check for missing fields
    if not all([oauth_token]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Use the oauth_token to fetch user info
    user_info = get_user_info_from_oauth(oauth_token)
    
    print("user Info ", user_info)
    
    if not user_info:
        return jsonify({"error": "Invalid OAuth token or unable to fetch user info"}), 400

    name = user_info.get('name')
    email = user_info.get('email')

    # Check if name and email are available
    if not all([name, email]):
        return jsonify({"error": "Missing user info"}), 400
    
    # Check if a connection with the same email already exists
    existing_connection = Connection.query.filter_by(email=email, company_id=current_company.id).first()
    
    if existing_connection:
        return jsonify({"error": "Connection already exists for this email"}), 400

    new_connection = Connection(name=name, email=email, oauth_token=oauth_token, company_id=current_company.id)
    print("new_connection:", new_connection)
    
    # Add the new Connection to the database
    db.session.add(new_connection)
    db.session.commit()
    
    return jsonify({"message": "Connection created!", "id": new_connection.id}), 201


def get_user_info_from_oauth(oauth_token):
    # Assuming OAuth provider API URL is 'https://api.oauthprovider.com/userinfo'
    headers = {"Authorization": f"Bearer {oauth_token}"}
    response = requests.get("https://www.googleapis.com/oauth2/v2/userinfo", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


def delete_Connection(current_company, id):
    company_id = current_company.id
    print("id :", id, "current company:", company_id)
    # Rename the variable to avoid conflict
    connection_to_delete = Connection.query.filter_by(id=id, company_id=company_id).first()
    if connection_to_delete:
        db.session.delete(connection_to_delete)
        db.session.commit()
        return jsonify({"message": "Connection deleted"}), 200
    return jsonify({"error": "Connection not found"}), 404



