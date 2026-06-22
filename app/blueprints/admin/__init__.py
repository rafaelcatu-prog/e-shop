from flask import Blueprint

public_bp = Blueprint(
    'public', 
    _name_, 
    template_folder='../../templates/public'
    )
from . import routes