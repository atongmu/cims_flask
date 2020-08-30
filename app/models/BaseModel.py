# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Boolean
from app.ext import db


class BaseModel(db.Model):
    """模型基类"""
    __abstract__ = True
    id = Column(Integer(), primary_key=True, autoincrement=True)
    create_date = Column(DateTime(), default=datetime.now,  comment=u"添加时间")
    update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now(), comment=u"修改时间")
    sort = Column(Integer(), default=0, comment=u"排序")
    is_show = Column(Boolean(), default=True, comment=u"是否显示")

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)

    def is_save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print 'save:' + e.message
            return False

    def is_update(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            print 'update:' + e.message
            return False

    def is_delete(self):
        try:
            self.is_show = True
            db.session.commit()
            return True
        except Exception as e:
            print 'show:' + e.message
            return False

    def is_remove(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print 'delete:' + e.message
            return False

    def count(self, _filters):
        try:
            count_number = db.session.query(self).filter(_filters).count()
            return count_number
        except Exception as e:
            print 'count:' + e.message
            return None
