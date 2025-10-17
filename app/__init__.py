from flask import Flask
from config.config import Config
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.destination_routes import destination_bp
    from app.routes.package_routes import package_bp
    from app.routes.reservation_routes import reservation_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(destination_bp)
    app.register_blueprint(package_bp)
    app.register_blueprint(reservation_bp)

    # Context processor para agregar año actual
    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.now().year}

    return app