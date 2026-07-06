from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
#configuracion de login manager
login_manager.login_view = 'auth.login'
login_manager.login_message = 'inicia sesion para continuar'
login_manager.login_message_category = 'warning'

@login_manager.user loader
def load_user(user_id)

    # Modelos
    from app.models import Usuario, Categoria, Producto, Pedido, DetallePedido

    # Blueprints
    from app.blueprints.public import public_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.admin import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app
