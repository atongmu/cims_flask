from flask import g, jsonify, make_response
from app.config import Config
from app.ext import token_auth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.models import Managers


@token_auth.verify_token
def verify_token(token):
    g.manager = None
    s = Serializer(Config.SECRET_KEY)
    try:
        data = s.loads(token)
    except BadSignature:
        print('token不正确')
        return False
    except SignatureExpired:
        print('token过期')
        return False
    user = Managers.query.get(data['id'])
    if user:
        g.manager = user
        return True
    return False


@token_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': '请登录'}), 401)
