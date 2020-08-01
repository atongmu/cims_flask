from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import GoodsDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("g_id", type=int, required=True, help="请输入请求参数")
parse_base.add_argument("name", type=str, required=True, help="请输入请求参数")
parse_base.add_argument("desc", type=str, help="请输入请求参数")


class UpdateGoodsResource(Resource):
    """修改物料"""

    def post(self):
        args = parse_base.parse_args()
        g_id = args.get("g_id")
        name = args.get("name")
        desc = args.get("desc")

        goods_default = GoodsDefault.query.get(g_id)
        goods_default.name = name
        if desc:
            goods_default.desc = desc

        if not goods_default.is_update():
            abort(404, msg="操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
