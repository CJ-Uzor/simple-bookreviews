from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()

def create_app(config_class = Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    from app.auth.routes import auth
    from app.main.routes import main
    from app.books.routes import books

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(books)

    return app
