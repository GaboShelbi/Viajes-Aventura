from flask import render_template, request, redirect, url_for, flash, session
from app.models.package_model import PackageModel
from app.models.destination_model import DestinationModel
from app.utils.auth_utils import admin_required

def list_packages():
    paquetes = PackageModel.get_all()
    return render_template('dashboard/paquetes.html', paquetes=paquetes)

@admin_required
def add_package():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        destinos = request.form.getlist('destinos')
        PackageModel.create(nombre, fecha_inicio, fecha_fin, destinos)
        flash('Paquete creado exitosamente', 'success')
        return redirect(url_for('package.list_packages'))
    destinos = DestinationModel.get_all()
    return render_template('dashboard/paquete_form.html', destinos=destinos, action='Agregar')

@admin_required
def edit_package(id):
    paquete = PackageModel.get_by_id(id)
    destinos = DestinationModel.get_all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        selected = request.form.getlist('destinos')
        PackageModel.update(id, nombre, fecha_inicio, fecha_fin, selected)
        flash('Paquete actualizado correctamente', 'info')
        return redirect(url_for('package.list_packages'))
    return render_template('dashboard/paquete_form.html', paquete=paquete, destinos=destinos, action='Editar')

@admin_required
def delete_package(id):
    PackageModel.delete(id)
    flash('Paquete eliminado', 'danger')
    return redirect(url_for('package.list_packages'))