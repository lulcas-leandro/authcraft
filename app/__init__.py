from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/main')
    def main_test():
        return "<h1>Main funcionando!</h1>"
    
    return app
