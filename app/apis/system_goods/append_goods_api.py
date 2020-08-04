# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import GoodsDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("name", required=True, help=u"请输入请求参数")
parse_base.add_argument("desc", help=u"请输入请求参数")


class AppendGoodsResource(Resource):
    """添加物料"""

    def post(self):
        args = parse_base.parse_args()
        name = args.get("name")
        desc = args.get("desc")
        goods = GoodsDefault.quser.filter(GoodsDefault.name == name).all()
        if goods:
            abort(404, msg=u"物料已存在")
        goods_default = GoodsDefault()
        goods_default.name = name
        if desc:
            goods_default.desc = desc

        if not goods_default.is_save():
            abort(404, msg=u"添加失败")
        data = {
            "status": HTTP_OK,
            "msg": u"添加成功"
        }
        return data
