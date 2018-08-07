from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login = LoginManager()

def create_app():

    app = Flask(__name__)

    login.init_app(app)
    
    from app.auth.routes import auth
    app.register_blueprint(auth)

    return app
