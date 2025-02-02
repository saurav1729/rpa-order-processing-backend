from flask import jsonify, request
from models.subdomain import Subdomain
from utils.db import db

def get_subdomains():
    subdomains = Subdomain.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": sub.id, "name": sub.name, "email": sub.email} for sub in subdomains]), 200

def add_subdomain():
    data = request.get_json()
    data['company_id']=current_company.id
    name = data.get('name')
    email = data.get('email')
    oauth_token = data.get('oauth_token')
    
    if not all([name,oauth_token]):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_subdomain = Subdomain( name=name, email=email, oauth_token=oauth_token)
    db.session.add(new_subdomain)
    db.session.commit()
    
    return jsonify({"message": "Subdomain created!", "id": new_subdomain.id}), 201

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

