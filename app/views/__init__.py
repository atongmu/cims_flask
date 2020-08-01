# -*- coding: utf-8 -*-
from app.models import Managers
from app.views.web.views import web


def init_views(app):
    app.register_blueprint(web)


def load_user(userid):
    return Managers.get(userid)
