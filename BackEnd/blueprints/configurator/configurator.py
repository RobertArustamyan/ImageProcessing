from flask import Blueprint

conf_bp = Blueprint('conf', __name__)


@conf_bp.route('/')
def index():
    return 'Test'