from flask import Blueprint
from app.controllers import reservation_controller

reservation_bp = Blueprint('reservation', __name__, url_prefix='/dashboard/reservas')

reservation_bp.route('/', methods=['GET'])(reservation_controller.list_reservations)
reservation_bp.route('/nueva', methods=['GET', 'POST'])(reservation_controller.add_reservation)
