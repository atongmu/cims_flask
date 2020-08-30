# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import String, Column, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel
from app.models.BaseMixinsModel import BaseMixinsModel


class GoodsDefault(BaseModel):
    """物料"""
    __tablename__ = "p_goods_default"
    name = Column(String(200), unique=True, nullable=False, comment=u"名称")
    stock = Column(Integer(), default=0, comment=u"库存")
    desc = Column(String(200), comment=u"描述")
    order = relationship("OrderDefault", backref="GoodsDefault", lazy="dynamic")

    def __repr__(self):
        return self.name


class OrderDefault(BaseMixinsModel):
    """物料订单"""
    __tablename__ = "p_order_default"
    create_date = Column(DateTime(), default=datetime.now, comment=u"添加时间")
    num = Column(Integer(), default=0, comment=u"数量")
    status = Column(Boolean(), default=True, comment=u"True进货，False出货")
    desc = Column(String(200), comment=u"描述")
    g_id = Column(Integer(), ForeignKey('p_goods_default.id'))
    goods = relationship("GoodsDefault", order_by='GoodsDefault.id', backref="OrderDefault")

    def __repr__(self):
        return self.desc
