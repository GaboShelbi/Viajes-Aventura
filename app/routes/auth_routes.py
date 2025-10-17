from flask import Blueprint
from app.controllers import auth_controller

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/', methods=['GET', 'POST'])(auth_controller.login)
auth_bp.route('/register', methods=['GET', 'POST'])(auth_controller.register)
auth_bp.route('/logout')(auth_controller.logout)
