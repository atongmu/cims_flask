# -*- coding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with, reqparse
from app.apis.api_constant import HTTP_OK
from app.models import GoodsDefault, OrderDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("g_id", type=int, required=True, help=u"请输入请求参数")

goods_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "stock": fields.Integer,
    "desc": fields.String,
    "create_date": fields.String
}
single_goods_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(goods_fields)
}


class FindGoodsResource(Resource):
    """查询物料"""

    @marshal_with(single_goods_fields)
    def get(self):
        args = parse_base.parse_args()
        g_id = args.get("g_id")
        system_goods = GoodsDefault.query.get(g_id)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": system_goods
        }
        return data
