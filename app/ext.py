# -*- coding: utf-8 -*-
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth, MultiAuth
# from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(use_native_unicode='utf8')
migrate = Migrate()
token_auth = HTTPTokenAuth('Token')
multi_auth = MultiAuth(token_auth)
# login_manager = LoginManager()


def init_ext(app):
    # 跨域
    CORS(app, supports_credentials=True)
    # 数据库
    db.init_app(app)
    migrate.init_app(app, db)
    # httpAuth方法
    from app.utils import auth_tools
    # 绑定登录视图的路由
    # login_manager.login_message = '请登录！'
    # login_manager.session_protection = 'strong'
    # login_manager.init_app(app)
    # from app.utils import login_tools
