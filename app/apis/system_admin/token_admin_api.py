from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.apis.system_admin.admin_utils import get_admin

parse_base = reqparse.RequestParser()
parse_base.add_argument("customer", type=str, required=True, help="请输入请求参数")
parse_base.add_argument("password", type=str, required=True, help="请输入请求参数")


class AdminTokenResource(Resource):
    """获取Token"""

    def get(self):
        args = parse_base.parse_args()
        customer = args.get("customer")
        pwd = args.get("password")
        manager = get_admin(customer)
        if not manager:
            abort(404, msg="用户不存在")
        if not manager.verify_password(pwd):
            abort(404, msg="用户名密码错误！")
        # 返回token值
        token = manager.generate_auth_token()
        data = {
            "status": HTTP_OK,
            "msg": "获取成功",
            "data": token.decode('ascii')
        }
        return data
