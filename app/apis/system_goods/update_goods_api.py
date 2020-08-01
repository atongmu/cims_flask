from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import GoodsDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("name", type=str, required=True, help="请输入请求参数")
parse_base.add_argument("desc", type=str, help="请输入请求参数")


class UpdateGoodsResource(Resource):
    """添加物料"""

    @multi_auth.login_required
    def post(self):
        args = parse_base.parse_args()
        name = args.get("name")
        desc = args.get("desc")

        goods_default = GoodsDefault()
        goods_default.name = name
        if desc:
            goods_default.desc = desc

        if not goods_default.is_save():
            abort(404, msg="添加失败")
        data = {
            "status": HTTP_OK,
            "msg": u"添加成功"
        }
        return data
