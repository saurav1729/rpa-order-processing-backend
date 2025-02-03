from flask import jsonify, request
from models.subdomain import Subdomain
from utils.db import db
import requests

def get_subdomains():
    subdomains = Subdomain.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": sub.id, "name": sub.name, "email": sub.email} for sub in subdomains]), 200

def add_subdomain(current_company):
    print("inside add_subdomain")
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
    
    # Create new subdomain entry
    # Create new subdomain entry
    new_subdomain = Subdomain(name=name, oauth_token=oauth_token, company_id=current_company.id)
    
    # Add the new subdomain to the database
    db.session.add(new_subdomain)
    db.session.commit()
    
    return jsonify({"message": "Subdomain created!", "id": new_subdomain.id}), 201

    print("inside add_subdomain")
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
    
    # Create new subdomain entry
    new_subdomain = ubdomain(name=name, email=email, oauth_token=oauth_token, company_id=current_company.id)
    
    # Add the new subdomain to the database
    db.session.add(new_subdomain)
    db.session.commit()
    
    return jsonify({"message": "Subdomain created!", "id": new_subdomain.id}), 201


def get_user_info_from_oauth(oauth_token):
    # Assuming OAuth provider API URL is 'https://api.oauthprovider.com/userinfo'
    headers = {"Authorization": f"Bearer {oauth_token}"}
    response = requests.get("https://www.googleapis.com/oauth2/v2/userinfo", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


def delete_subdomain(id):
    subdomain = Subdomain.query.filter_by(id=id, user_id=user_id).first()
    if subdomain:
        db.session.delete(subdomain)
        db.session.commit()
        return jsonify({"message": "Subdomain deleted"}), 200
    return jsonify({"error": "Subdomain not found"}), 404

def update_subdomain(id):
    subdomain = Subdomain.query.filter_by(id=id, user_id=user_id).first()
    if not subdomain:
        return jsonify({"error": "Subdomain not found"}), 404
    
    data = request.json
    subdomain.name = data.get('name', subdomain.name)
    subdomain.email = data.get('email', subdomain.email)
    subdomain.oauth_token = data.get('oauth_token', subdomain.oauth_token)
    
    db.session.commit()
    return jsonify({"message": "Subdomain updated", "id": subdomain.id}), 200

