# -*- coding: utf-8 -*-
from datetime import datetime

from flask_restful import Resource, fields, marshal_with, reqparse
from app.apis.api_constant import HTTP_OK
from app.models import OrderDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("status", type=int, required=True, help=u"请输入请求参数")
parse_base.add_argument("g_id", required=True, help=u"请输入请求参数")
parse_base.add_argument("page_no", type=int, required=True, help=u"请输入请求参数")
parse_base.add_argument("page_size", type=int, required=True, help=u"请输入请求参数")

order_fields = {
    "id": fields.Integer,
    "status": fields.Boolean,
    "num": fields.Integer,
    "desc": fields.String,
    "create_date": fields.String,
}
pages_order = {
    "pages": fields.Integer,
    "total": fields.Integer,
    "items": fields.List(fields.Nested(order_fields)),
}
single_order_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(pages_order)
}


class FindOrderResource(Resource):
    """查询物料订单"""

    @marshal_with(single_order_fields)
    def get(self):
        args = parse_base.parse_args()
        status = args.get("status")
        g_id = args.get("g_id")
        page_no = args.get("page_no")
        page_size = args.get("page_size")
        system_page = OrderDefault.query.filter(OrderDefault.status == status, OrderDefault.g_id == g_id).order_by(
            OrderDefault.create_date.desc()).paginate(page_no, page_size)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": system_page
        }
        return data
