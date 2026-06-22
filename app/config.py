import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://ecommerce_user:12345@localhost/ecommerce_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
