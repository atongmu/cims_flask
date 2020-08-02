# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth
from app.models import GoodsDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("g_id", type=int, required=True, help=u"请输入请求参数")


class RemoveGoodsResource(Resource):
    """删除物料"""

    def post(self):
        args = parse_base.parse_args()
        g_id = args.get("g_id")

        goods_default = GoodsDefault.query.get(g_id)

        if not goods_default:
            abort(404, msg=u"无此商品")

        if not goods_default.is_remove():
            abort(404, msg=u"操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
