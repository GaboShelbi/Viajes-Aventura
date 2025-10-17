from flask import render_template, request, redirect, url_for, flash, session
from app.models.destination_model import DestinationModel
from app.utils.auth_utils import admin_required

def list_destinations():
    destinos = DestinationModel.get_all()
    return render_template('dashboard/destinos.html', destinos=destinos)

@admin_required
def add_destination():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        actividades = request.form['actividades']
        costo = request.form['costo']
        DestinationModel.create(nombre, descripcion, actividades, costo)
        flash('Destino agregado correctamente', 'success')
        return redirect(url_for('destination.list_destinations'))
    return render_template('dashboard/destino_form.html', action='Agregar')

@admin_required
def edit_destination(id):
    destino = DestinationModel.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        actividades = request.form['actividades']
        costo = request.form['costo']
        DestinationModel.update(id, nombre, descripcion, actividades, costo)
        flash('Destino actualizado correctamente', 'info')
        return redirect(url_for('destination.list_destinations'))
    return render_template('dashboard/destino_form.html', destino=destino, action='Editar')

@admin_required
def delete_destination(id):
    DestinationModel.delete(id)
    flash('Destino eliminado', 'danger')
    return redirect(url_for('destination.list_destinations'))