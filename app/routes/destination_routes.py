from flask import Blueprint
from app.controllers import destination_controller

destination_bp = Blueprint('destination', __name__, url_prefix='/dashboard/destinos')

destination_bp.route('/', methods=['GET'])(destination_controller.list_destinations)
destination_bp.route('/nuevo', methods=['GET', 'POST'])(destination_controller.add_destination)
destination_bp.route('/editar/<int:id>', methods=['GET', 'POST'])(destination_controller.edit_destination)
destination_bp.route('/eliminar/<int:id>', methods=['GET'])(destination_controller.delete_destination)
