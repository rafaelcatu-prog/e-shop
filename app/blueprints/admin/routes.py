from flask import render_template
from . import admin_bp
from flask_login import login_required
from decorators import login_required


@admin_bp.route('/index')
def index():
    return render_template("admin/index.html")


@admin_bp.route('/productos')
def admin_productos():
    """Ruta: /admin/productos"""
    return render_template('admin/productos.html')


@admin_bp.route('/clientes')
def admin_clientes():
    """Ruta: /admin/clientes"""
    return render_template('admin/clientes.html')


@admin_bp.route('/pedidos')
def admin_pedidos():
    """Ruta: /admin/pedidos"""
    return render_template('admin/pedidos.html')