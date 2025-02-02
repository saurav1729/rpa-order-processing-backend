import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ORCHESTRATOR_API_KEY = os.getenv('ORCHESTRATOR_API_KEY', 'your_orchestrator_api_key')
    PORT = os.getenv('PORT')
