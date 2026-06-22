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


rafaelcatu@PC:~/web/e-shop$ tree -a -I "venv|.git|env|.env"
.
├── app
│   ├── blueprints
│   │   ├── admin
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   └── public
│   │       ├── __init__.py
│   │       └── routes.py
│   ├── config.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── pedido.py
│   │   ├── producto.py
│   │   └── usuario.py
│   ├── static
│   │   ├── css
│   │   └── js
│   └── templates
│       ├── admin
│       ├── auth
│       ├── base.html
│       └── public
├── .gitignore
├── requirements.txt
└── run.py

14 directories, 16 files
rafaelcatu@PC:~/web/e-shop$ 
