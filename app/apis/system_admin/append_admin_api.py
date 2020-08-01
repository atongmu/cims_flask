from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.apis.system_admin.admin_utils import get_admin
from app.ext import multi_auth
from app.models import Managers

parse_base = reqparse.RequestParser()
parse_base.add_argument("customer", type=str, required=True, help="请输入请求参数")
parse_base.add_argument("password", type=str, required=True, help="请输入请求参数")


class AdminAppendResource(Resource):
    """管理员注册"""

    @multi_auth.login_required
    def post(self):
        args = parse_base.parse_args()
        customer = args.get("customer")
        pwd = args.get("password")
        manager = get_admin(customer)
        if manager:
            abort(404, msg="用户已存在")
        new_manager = Managers()
        new_manager.users_name = customer
        new_manager.password = pwd
        if not new_manager.is_save():
            abort(404, msg="用户注册失败")
        data = {
            "status": HTTP_OK,
            "msg": u"注册成功"
        }
        return data
