# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Column
from app.ext import db


class BaseMixinsModel(db.Model):
    """模型基类"""
    __abstract__ = True
    id = Column(Integer(), primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super(BaseMixinsModel, self).__init__(*args, **kwargs)

    def is_save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print('save:' + e.message)
            return False

    def is_update(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            print('update:' + e.message)
            return False

    def is_delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print('delete:' + e.message)
            return False

    def count(self, _filters):
        try:
            count_number = db.session.query(self).filter(_filters).count()
            return count_number
        except Exception as e:
            print('count:' + e.message)
            return None
