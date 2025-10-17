from flask import render_template, request, redirect, url_for, session, flash
from app.models.reservation_model import ReservationModel
from app.models.package_model import PackageModel

def list_reservations():
    reservas = ReservationModel.get_all()
    return render_template('dashboard/reservas.html', reservas=reservas)

def add_reservation():
    paquetes = PackageModel.get_all()
    if request.method == 'POST':
        user_id = session['user_id']
        paquete_id = request.form['paquete_id']
        fecha_reserva = request.form['fecha_reserva']
        ReservationModel.create(user_id, paquete_id, fecha_reserva)
        flash('Reserva realizada con éxito', 'success')
        return redirect(url_for('reservation.list_reservations'))
    return render_template('dashboard/reserva_form.html', paquetes=paquetes)
