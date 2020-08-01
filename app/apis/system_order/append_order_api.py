from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import GoodsDefault, OrderDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("g_id", type=int, required=True, help="请输入请求参数")
parse_base.add_argument("status", type=bool, required=True, help="请输入请求参数")
parse_base.add_argument("num", type=int, required=True, help="请输入请求参数")
parse_base.add_argument("desc", type=int, help="请输入请求参数")


class AppendOrderResource(Resource):
    """添加物料"""

    @multi_auth.login_required
    def post(self):
        args = parse_base.parse_args()
        g_id = args.get("g_id")
        status = args.get("status")
        num = args.get("num")
        desc = args.get("desc")

        goods_default = GoodsDefault.query.get(g_id)
        if goods_default is None:
            abort(404, msg="无此商品")
        # 修改库存
        if status:
            goods_default.stock += num
        else:
            goods_default.stock -= num

        if not goods_default.is_update():
            abort(404, msg="操作失败")

        # 创建订单
        order_default = OrderDefault()
        order_default.g_id = g_id
        order_default.status = status
        order_default.num = num
        if desc:
            order_default.desc = desc

        if not order_default.is_save():
            abort(404, msg="操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
