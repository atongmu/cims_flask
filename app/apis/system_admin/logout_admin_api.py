from flask_restful import Resource, reqparse
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth

parse_base = reqparse.RequestParser()
parse_base.add_argument("Authorization", location='headers', help="请输入请求参数")


class AdminLogoutResource(Resource):
    """管理员退出"""

    @multi_auth.login_required
    def get(self):

        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
