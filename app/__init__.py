from flask import Flask
from flask sqlalchemy import SQLAlchemy
from flask migrate import Migrate
from app.config import Config

db = SQLAlchemy()
Migrate = Migrate()

def create_app():
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate


