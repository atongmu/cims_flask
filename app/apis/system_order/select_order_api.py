from datetime import datetime

from flask_restful import Resource, fields, marshal_with, reqparse
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import OrderDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("status", type=bool, help="请输入请求参数")
parse_base.add_argument("create_date", type=str, help="请输入请求参数")
parse_base.add_argument("page_no", type=int, required=True, help="请输入请求参数")
parse_base.add_argument("page_size", type=int, required=True, help="请输入请求参数")

goods_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "update_date": fields.String,
    "stock": fields.Integer,
    "desc": fields.String,
}
order_fields = {
    "id": fields.Integer,
    "status": fields.Boolean,
    "num": fields.Integer,
    "desc": fields.String,
    "create_date": fields.String,
    "goods": fields.Nested(goods_fields)
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


class SelectOrderResource(Resource):
    """查询物料订单"""
    decorators = [multi_auth.login_required]

    @marshal_with(single_order_fields)
    def get(self):
        args = parse_base.parse_args()
        status = args.get("status")
        create_date = args.get("create_date")
        page_no = args.get("page_no")
        page_size = args.get("page_size")
        _condition = []
        if status is not None:
            _condition.append(OrderDefault.status == status)
        if create_date is not None:
            # 时间筛选
            if '/' in create_date:
                record_date = datetime.strptime(create_date, "%Y/%m/%d")
            else:
                record_date = datetime.strptime(create_date, "%Y-%m-%d")
            _condition.append(OrderDefault.name.create_date == record_date)
        if _condition:
            system_page = OrderDefault.query.filter(*_condition).order_by(OrderDefault.create_date.desc()).paginate(
                page_no, page_size)
        else:
            system_page = OrderDefault.query.order_by(OrderDefault.create_date.desc()).paginate(page_no, page_size)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": system_page
        }
        return data
