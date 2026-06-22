from flask import render_template
from . import admin_bp

@admin_bp.route('/')
def admin ():
    return render_template('admin/index.html')

@admin_bp.route('/tienda')
def tienda():
    return render_template('public/tienda.html')

@admin_bp.route('/contacto')
def contacto():
    return render_template('public/tienda.html ')

    @admin_bp.route('/admin/clientes')
    def pedidos():
        return render_template('admin/pedidos.html')
