from flask import render_template
from . import admin_bp
from flask_login import login_required
from .decorators import admin_requerido


@admin_bp.route('/dashboard')
@login_required
@admin_requerido
def dashboard():
    return render_template('admin/home.html')


@admin_bp.route('/productos')
@login_required
@admin_requerido
def productos():
    return render_template('admin/productos.html')


@admin_bp.route('/clientes')
@login_required
@admin_requerido
def clientes():
    return render_template('admin/clientes.html')


@admin_bp.route('/pedidos')
@login_required
@admin_requerido
def pedidos():
    return render_template('admin/pedidos.html')