from flask_restful import Api

from app.apis.system_order.append_order_api import AppendOrderResource

system_order_api = Api(prefix="/api/order_api", catch_all_404s=True)
system_order_api.add_resource(AppendOrderResource, "/append_order")