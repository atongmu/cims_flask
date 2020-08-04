# -*- coding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with, reqparse
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import GoodsDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("name", type=str, help=u"请输入请求参数")
parse_base.add_argument("page_no", type=int, required=True, help=u"请输入请求参数")
parse_base.add_argument("page_size", type=int, required=True, help=u"请输入请求参数")

goods_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "update_date": fields.String,
    "stock": fields.Integer,
    "desc": fields.String,
}
pages_goods = {
    "pages": fields.Integer,
    "total": fields.Integer,
    "items": fields.List(fields.Nested(goods_fields)),
}
single_goods_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(pages_goods)
}


class SelectGoodsResource(Resource):
    """查询物料"""

    @marshal_with(single_goods_fields)
    def get(self):
        args = parse_base.parse_args()
        name = args.get("name")
        page_no = args.get("page_no")
        page_size = args.get("page_size")
        _condition = []
        if name is not None:
            _condition.append(GoodsDefault.name.like("%" + name + "%"))
        system_page = GoodsDefault.query.filter(*_condition).order_by(GoodsDefault.stock.asc()).paginate(page_no,
                                                                                                         page_size)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": system_page
        }
        return data
