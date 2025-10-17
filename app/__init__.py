from flask import Flask
from config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importa y registra los blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
