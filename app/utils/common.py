# -*- coding: utf-8 -*-
import hashlib

ALLOWED_file_EXTENSIONS = set(['md', 'MD', 'word', 'txt', 'py', 'java', 'c', 'c++', 'xlsx'])
ALLOWED_photo_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG', 'JPEG', 'PNG', 'gif', 'GIF'])


# md5 32位加密
def md5(strs):
    m2 = hashlib.md5()
    m2.update(strs.encode(encoding="UTF-8"))
    return m2.hexdigest()


def verifyMd5(strs, hash_strs):
    if md5(strs) == hash_strs:
        return True
    else:
        return False


# 生成随机数量
from random import Random


def random_str(randomlength):
    _str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        _str += chars[random.randint(0, length)]
    return _str


def allowed_photo(filename):
    return filename in ALLOWED_photo_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_file_EXTENSIONS


# 截取字符串
def getstrsplit(beginint, strs):
    lens = len(strs)
    return strs[beginint:lens]


def verity_password(originPassword, password):
    newpassword = md5(originPassword)
    return password == newpassword
