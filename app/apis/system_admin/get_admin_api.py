from flask import g
from flask_restful import Resource, fields, marshal_with
from app.apis.api_constant import HTTP_OK
from app.ext import multi_auth

actions_fields = {
    "action_id": fields.String,
    "action_desc": fields.String,
    "action_key": fields.String
}
permission_fields = {
    "permission_id": fields.String,
    "permission_key": fields.String,
    "permission_name": fields.String,
    "actions": fields.List(fields.String)
}
role_fields = {
    "role_name": fields.String,
    "permission": fields.List(fields.Nested(permission_fields)),
}
admin_fields = {
    "id": fields.Integer,
    "avatar": fields.String,
    "users_email": fields.String,
    "users_name": fields.String,
    "is_administrator": fields.Integer,
    "mobile_phone": fields.String(),
    "role": fields.Nested(role_fields),
}
single_admin_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(admin_fields)
}


class AdminInfoResource(Resource):
    """用户详情"""
    decorators = [multi_auth.login_required]

    @marshal_with(single_admin_fields)
    def get(self):
        current_user = g.manager
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": current_user
        }
        return data
