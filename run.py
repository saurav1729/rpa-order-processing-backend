import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils.config import Config
from flask_cors import CORS
# from routes import auth_routes, connection_routes, email_routes
from utils.db import db


app = Flask(__name__)
app.config.from_object(Config)


CORS(app,supports_credentials=True) 

# Initialize DB and Migrate
db.init_app(app)  
migrate = Migrate(app, db)

from models.user import User  # Add this line if you have separate model files
from models.company import Company

# Test database connection
try:
    # Try to establish a connection by performing a simple query or test
    with app.app_context():
        db.engine.connect()
        print("Database connection successful.")
except Exception as e:
    print("Database connection failed.")
    print(f"Error: {str(e)}")


from routes.auth_routes import auth_bp as auth_routes
from routes.user_routes import user_bp as user_routes
from routes.Connection_routes import Connection_bp as Connection_routes
from routes.Config_routes import Config_bp as Config_routes
from routes.index import api as api

app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(user_routes, url_prefix='/company')
app.register_blueprint(Connection_routes, url_prefix='/company')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(Config_routes, url_prefix = '/Config')

if __name__ == "__main__":
    port = int(Config.PORT) if Config.PORT else 8080  
    app.run(host="0.0.0.0", port=port,debug=True,use_reloader=True)
 