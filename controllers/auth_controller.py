import datetime
import jwt
from flask import request, jsonify, make_response, Blueprint
from models.company import Company
from models.user import User
from utils.db import db
from utils.config import Config
from werkzeug.security import check_password_hash

# Create a Blueprint for authentication
auth_bp = Blueprint("auth", __name__)

def generate_token(entity, is_company=False):
    """Generate JWT token for either company or user."""
    payload = {
        "id": entity.id,
        "email": entity.email,
        "is_company": is_company,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    if not is_company:
        payload["company_id"] = entity.company_id
        payload["role"] = entity.role
    
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")  # No alias needed


def unified_login():
    """Login for both company and user"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Try to find a company with the given email
    company = Company.query.filter_by(email=email).first()
    if company and check_password_hash(company.password, password):
        token = generate_token(company, is_company=True)
        response_data = {
            "message": "Company login successful",
            "data": company.serialize(),
            "token": token,
            "is_company": True
        }
    else:
        # If not a company, try to find a user
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            token = generate_token(user)
            response_data = {
                "message": "User login successful",
                "data": user.serialize(),
                "token": token,
                "is_company": False
            }
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    
    response = make_response(jsonify(response_data))
    response.set_cookie("auth_token", token, httponly=True, secure=True, samesite="Strict")
    return response, 200

def register_company():
    """Register a new company"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    address = data.get('address')
    contact_number = data.get('contact_number')

    if Company.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    company = Company(
        email=email, name=name, 
        address=address, contact_number=contact_number
    )
    company.set_password(password)

    db.session.add(company)
    db.session.commit()

    token = generate_token(company, is_company=True)
    
    response_data = {
        "message": "Company registered successfully",
        "data": company.serialize(),
        "token": token,
        "is_company": True
    }

    response = make_response(jsonify(response_data))
    response.set_cookie("auth_token", token, httponly=True, secure=True)
    return response, 201

def register_user():
    """Register a new user"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    role = data.get('role')
    company_id = data.get('company_id')
    
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        email=email, first_name=first_name, last_name=last_name,
        role=role, company_id=company_id
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    token = generate_token(user)
    
    response_data = {
        "message": "User registered successfully",
        "data": user.serialize(),
        "token": token,
        "is_company": False
    }

    response = make_response(jsonify(response_data))
    response.set_cookie("auth_token", token, httponly=True, secure=True)
    return response, 201
