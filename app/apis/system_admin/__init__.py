# -*- coding: utf-8 -*-
from flask_restful import Api

from app.apis.system_admin.append_admin_api import AdminAppendResource
from app.apis.system_admin.get_admin_api import AdminInfoResource
from app.apis.system_admin.logout_admin_api import AdminLogoutResource
from app.apis.system_admin.token_admin_api import AdminTokenResource

system_admin_api = Api(prefix="/api/manager_api", catch_all_404s=True)

system_admin_api.add_resource(AdminTokenResource, "/manager_token")
system_admin_api.add_resource(AdminLogoutResource, "/manager_logout")
system_admin_api.add_resource(AdminAppendResource, "/manager_append")
system_admin_api.add_resource(AdminInfoResource, "/manager_info")
