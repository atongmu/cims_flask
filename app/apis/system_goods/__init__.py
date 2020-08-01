from flask_restful import Api

from app.apis.system_goods.append_goods_api import AppendGoodsResource
from app.apis.system_goods.find_goods_api import FindGoodsResource
from app.apis.system_goods.remove_goods_api import RemoveGoodsResource
from app.apis.system_goods.select_goods_api import SelectGoodsResource
from app.apis.system_goods.update_goods_api import UpdateGoodsResource

system_goods_api = Api(prefix="/api/goods_api", catch_all_404s=True)

system_goods_api.add_resource(AppendGoodsResource, "/append_goods")
system_goods_api.add_resource(UpdateGoodsResource, "/update_goods")
system_goods_api.add_resource(RemoveGoodsResource, "/remove_goods")
system_goods_api.add_resource(SelectGoodsResource, "/select_goods")
system_goods_api.add_resource(FindGoodsResource, "/find_goods")
