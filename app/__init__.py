from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from utils.config import Config



def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('config.Config')

    from routes.index import api
    # from routes.auth_routes import auth_bp
    # from app.routes.connection_routes import connection_bp
    # from app.routes.email_routes import email_bp 
    app.register_blueprint(api, url_prefix='/api')
    # app.register_blueprint(auth_bp, url_prefix="/api")
    # app.register_blueprint(connection_bp, url_prefix="/api")
    # app.register_blueprint(email_bp, url_prefix="/api")

    return app
