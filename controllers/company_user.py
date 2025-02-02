from flask import request, jsonify
from models.user import User
from utils.db import db
from controllers.auth_controller import register_user

def add_user(current_company):
    """Add a new user to the company"""
    data = request.get_json()
    data['company_id'] = current_company.id
    print(data)
    
    response, status_code = register_user()
    
    if status_code == 201:
        return jsonify({"message": "User added successfully", "data": response.json['data']}), 201
    
    return response, status_code

def delete_user(current_company, user_id):
    """Delete a user from the company"""
    user = User.query.filter_by(id=user_id, company_id=current_company.id).first()
    
    if not user:
        return jsonify({"message": "User not found"}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

def update_user(current_company, user_id):
    """Update a user in the company"""
    print(current_company, user_id)
    user = User.query.filter_by(id=user_id, company_id=current_company.id).first()
    
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    
    # Update user fields
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']
    if 'password' in data:
        user.set_password(data['password'])

    db.session.commit()

    return jsonify({"message": "User updated successfully", "data": user.serialize()}), 200

def get_company_users(current_company):
    """Get all users for the company"""
    users = User.query.filter_by(company_id=current_company.id).all()
    return jsonify({"users": [user.serialize() for user in users]}), 200

