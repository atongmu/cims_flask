from flask_restful import Resource, fields, marshal_with, reqparse
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import GoodsDefault, OrderDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("g_id", type=str, help="请输入请求参数")
parse_base.add_argument("page_no", type=int, required=True, help="请输入请求参数")
parse_base.add_argument("page_size", type=int, required=True, help="请输入请求参数")

order_fields = {
    "id": fields.Integer,
    "status": fields.Boolean,
    "num": fields.Integer,
    "desc": fields.String,
    "create_date": fields.String
}
pages_goods = {
    "pages": fields.Integer,
    "total": fields.Integer,
    "items": fields.List(fields.Nested(order_fields)),
}
single_goods_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(pages_goods)
}


class FindGoodsResource(Resource):
    """查询物料"""

    @marshal_with(single_goods_fields)
    def get(self):
        args = parse_base.parse_args()
        g_id = args.get("g_id")
        page_no = args.get("page_no")
        page_size = args.get("page_size")
        system_goods = GoodsDefault.query.get(g_id)
        system_page = system_goods.order.order_by(OrderDefault.create_date.desc()).paginate(page_no, page_size)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": system_page
        }
        return data
