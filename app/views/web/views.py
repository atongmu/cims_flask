from flask import Blueprint

web = Blueprint('main', __name__)


@web.route("/")
def index():
    return 'index'
