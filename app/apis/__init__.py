from app.apis.system_admin import system_admin_api
from app.apis.system_goods import system_goods_api
from app.apis.system_order import system_order_api


def init_views_api(app):
    system_admin_api.init_app(app)
    system_goods_api.init_app(app)
    system_order_api.init_app(app)
