from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import String, Column,Text
from werkzeug.security import generate_password_hash, check_password_hash

from app.config import Config
from app.utils.common import md5
from app.models.BaseModel import BaseModel


class Managers(BaseModel):
    """管理员登录表"""
    __tablename__ = "b_manager"
    users_name = Column(String(200), unique=True)
    _password = Column(String(100), nullable=True)
    users_avatar = Column(Text(), nullable=True)

    @property
    def password(self):
        raise Exception(u"访问不了")

    @password.setter
    def password(self, password_val):
        self._password = generate_password_hash(password_val)

    # 校验密码方法
    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(Config.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @property
    def avatar(self):
        """用户头像"""
        avatar_url = self.users_avatar
        if avatar_url is None:
            digest = md5(self.users_name)
            avatar_url = 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, 46)
        return avatar_url
