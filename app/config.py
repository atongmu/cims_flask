# -*- coding: utf-8 -*-
import logging


def get_db_url(dbinfo):
    engine = dbinfo.get('ENGINE') or 'sqlite'
    driver = dbinfo.get('DRIVER') or 'sqlite'
    user = dbinfo.get('USER') or 'sqlite'
    password = dbinfo.get('PASSWORD') or ''
    host = dbinfo.get('HOST') or ''
    port = dbinfo.get('PORT') or ''
    name = dbinfo.get('NAME') or ''
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_NAME = 'adminCookie'
    FLASK_ADMIN_SWATCH = 'cerulean'
    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
    SECRET_KEY = 'blpZaN1R9M2w0qnK'


class DevelopmentConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1234",
        "HOST": "127.0.0.1",
        "PORT": "3309",
        "NAME": "flask_cims"
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DefaultConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "zhangAI000829",
        "HOST": "127.0.0.1",
        "PORT": "3309",
        "NAME": "yuyue"
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DefaultConfig
}
