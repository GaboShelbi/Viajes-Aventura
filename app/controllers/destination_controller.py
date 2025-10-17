from flask import render_template, request, redirect, url_for, flash
from app.models.destination_model import DestinationModel

def list_destinations():
    destinos = DestinationModel.get_all()
    return render_template('dashboard/destinos.html', destinos=destinos)

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

def delete_destination(id):
    DestinationModel.delete(id)
    flash('Destino eliminado', 'danger')
    return redirect(url_for('destination.list_destinations'))
