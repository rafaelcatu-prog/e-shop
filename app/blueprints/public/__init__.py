from flask import Blueprint

public bp = Blueprint(
    'public',
    __name__,
    template_folder='../../templates/public'
)
from. import routes
