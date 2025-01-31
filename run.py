import os
from app import create_app
from config import Config

app = create_app()

if __name__ == "__main__":
    port = int(Config.PORT) if Config.PORT else 8080  
    app.run(host="0.0.0.0", port=port)
