from flask import render_template, request, redirect, url_for, flash, session
from app.models.reservation_model import ReservationModel
from app.models.package_model import PackageModel

def list_reservations():
    user_id = session.get('user_id')
    rol = session.get('user_rol')
    if rol == 'admin':
        reservas = ReservationModel.get_all()
    else:
        reservas = ReservationModel.get_by_user(user_id)
    return render_template('dashboard/reservas.html', reservas=reservas)

def add_reservation():
    if request.method == 'POST':
        paquete_id = request.form['paquete_id']
        fecha_reserva = request.form['fecha_reserva']
        user_id = session['user_id']
        ReservationModel.create(user_id, paquete_id, fecha_reserva)
        flash('Reserva realizada exitosamente', 'success')
        return redirect(url_for('reservation.list_reservations'))
    paquetes = PackageModel.get_all()
    return render_template('dashboard/reserva_form.html', paquetes=paquetes)