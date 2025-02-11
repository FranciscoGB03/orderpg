from flask import Flask
from flask_cors import CORS
from app.routes.order_routes import order_bp
from app.routes.menu_routes import menu_bp
from app.routes.ping_routes import ping_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para todas las rutas
    
    # Registrar Blueprints (módulos de rutas)
    app.register_blueprint(order_bp, url_prefix="/api")
    app.register_blueprint(menu_bp, url_prefix="/api")
    app.register_blueprint(ping_bp, url_prefix="/")

    return app
