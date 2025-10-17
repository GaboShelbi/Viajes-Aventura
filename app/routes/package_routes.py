from flask import Blueprint
from app.controllers import package_controller

package_bp = Blueprint('package', __name__, url_prefix='/dashboard/paquetes')

package_bp.route('/', methods=['GET'])(package_controller.list_packages)
package_bp.route('/nuevo', methods=['GET', 'POST'])(package_controller.add_package)
package_bp.route('/eliminar/<int:id>', methods=['GET'])(package_controller.delete_package)
