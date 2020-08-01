# -*- coding: utf-8 -*-
import os

HTTP_OK = 200
HTTP_CREATE_OK = 201

ACTION_LOGIN = "login"
ACTION_LOGOUT = "logout"

ACTION_INFO = "info"
ACTION_APPEND = "append"
ACTION_UPDATE = "update"
ACTION_DELETE = "delete"
ACTION_ALL = "all"
ACTION_PAGE = "page"
ACTION_STATUS = "status"
ACTION_COUNT = "count"

IMAGES_PATH = "app/static/images/server"
IMAGES_LINK = "/static/images/server"
BASE_PATH = os.path.abspath(os.path.dirname(__name__))
TOKEN_VALUE = 'Vue-Admin-Base-Token'
API_TOKEN_VALUE = 'Vue-Customer-Base-Token'

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 允许大小16MB
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])  # 允许文件
