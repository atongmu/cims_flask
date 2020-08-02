# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from app.config import config
from app.ext import init_ext
from app.middleware import load_middleware
from app import models


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 跨域
    cors = CORS(app)

    # 加载第三方库
    init_ext(app)

    # 加载中间件
    load_middleware(app)

    # 加载蓝图
    from app.views import init_views
    init_views(app)

    # 加载api接口
    from app.apis import init_views_api
    init_views_api(app)

    return app
