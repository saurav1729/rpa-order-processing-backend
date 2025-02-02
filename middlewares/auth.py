from functools import wraps
from flask import request, jsonify
import jwt
from utils.config import Config
from models.company import Company
from models.user import User

def get_token():
    """Get token from header or cookie"""
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        return token.split()[1]
    return request.cookies.get('auth_token')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_entity = None
            if data.get('is_company'):
                current_entity = Company.query.filter_by(id=data['id']).first()
            else:
                current_entity = User.query.filter_by(id=data['id']).first()
            
            if not current_entity:
                raise ValueError("Entity not found")
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except (jwt.InvalidTokenError, ValueError):
            return jsonify({"message": "Token is invalid"}), 401

        return f(current_entity, *args, **kwargs)

    return decorated

def company_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            print("hello", data)
            if not data.get('is_company'):
                return jsonify({"message": "Company access required"}), 403
            current_company = Company.query.filter_by(id=data['id']).first()
            if not current_company:
                raise ValueError("Company not found")
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except (jwt.InvalidTokenError, ValueError):
            return jsonify({"message": "Token is invalid"}), 401

        return f(current_company, *args, **kwargs)

    return decorated

def company_or_admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            # Decode the JWT token
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_entity = None

            # If the entity is a company
            if data.get('is_company'):
                current_entity = Company.query.filter_by(id=data['id']).first()

            # If it's a user, check their associated company and role
            elif not data.get('is_company'):
                current_entity = User.query.filter_by(id=data['id']).first()

                if current_entity:
                    # Verify the user's associated company
                    company = Company.query.filter_by(id=current_entity.company_id).first()
                    if not company:
                        raise ValueError("User's associated company not found")
                else:
                    raise ValueError("User not found")

            if not current_entity:
                raise ValueError("Entity not found")

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except (jwt.InvalidTokenError, ValueError):
            return jsonify({"message": "Token is invalid"}), 401

        # Allow the decorated function to access the current entity (company or user)
        return f(current_entity, *args, **kwargs)

    return decorated
