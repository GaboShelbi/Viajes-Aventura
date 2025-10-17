from flask import render_template, request, redirect, url_for, flash
from app.models.package_model import PackageModel
from app.models.destination_model import DestinationModel

def list_packages():
    paquetes = PackageModel.get_all()
    return render_template('dashboard/paquetes.html', paquetes=paquetes)

def add_package():
    destinos = DestinationModel.get_all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        destinos_ids = request.form.getlist('destinos')
        PackageModel.create(nombre, fecha_inicio, fecha_fin, destinos_ids)
        flash('Paquete turístico creado exitosamente', 'success')
        return redirect(url_for('package.list_packages'))
    return render_template('dashboard/paquete_form.html', destinos=destinos, action='Agregar')

def delete_package(id):
    PackageModel.delete(id)
    flash('Paquete eliminado correctamente', 'danger')
    return redirect(url_for('package.list_packages'))
