from flask import Blueprint, Flask, redirect, request, jsonify
from controllers.auth_controller import register_company, unified_login
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import requests
import os


auth_bp = Blueprint('auth_routes', __name__)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


AUTH_URL = os.getenv('AUTH_URL')
TOKEN_URL = os.getenv('TOKEN_URL')



# Add Gmail scopes for requesting email access
SCOPES = "openid profile email https://mail.google.com/ https://www.googleapis.com/auth/gmail.modify"



def auth_google():
    # Generate Google OAuth URL with Gmail scopes
    auth_url = (
        f"{AUTH_URL}?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"response_type=code&"
        f"scope={SCOPES}&"
        f"access_type=offline&"
        f"prompt=consent"
    )
    print(auth_url)
    return redirect(auth_url)


def auth_google_callback():
    # Exchange authorization code for tokens
    code = request.args.get('code')
    
    try:
        # Get tokens from Google
        token_response = requests.post(TOKEN_URL, data={
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code'
        }).json()

        # Verify ID token
        id_info = id_token.verify_oauth2_token(
            token_response['id_token'],
            google_requests.Request(),
            CLIENT_ID
        )

        # Return token to frontend
        return redirect(f'https://astra-rpa.vercel.app/u/Connection?token={token_response["access_token"]}')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400




auth_bp.route('/register', methods=['POST'])(register_company)
auth_bp.route('/login', methods=['POST'])(unified_login)


# Route to initiate Google OAuth
auth_bp.route('/google', methods=['GET'])(auth_google)



# Route for Google OAuth callback
auth_bp.route('/google/callback', methods=['GET'])(auth_google_callback)


