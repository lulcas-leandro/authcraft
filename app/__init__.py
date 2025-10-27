from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça login para acessar esta página'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    try:
        from app.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')
        print('Blueprint auth registrado com sucesso!')

    except Exception as e:
        print(f'Blueprint auth não foi registrado, erro: {e}')
