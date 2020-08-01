from datetime import datetime
from sqlalchemy import String, Column, Boolean, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from app.models.BaseMixinsModel import BaseMixinsModel
from app.models import BaseModel


class GoodsDefault(BaseModel):
    """物料"""
    __tablename__ = "p_goods_default"
    name = Column(String(200), comment="名称")
    stock = Column(Integer(), default=0, comment="库存")
    desc = Column(String(200), comment="描述")
    order = relationship("OrderDefault", back_populates="GoodsDefault", lazy="dynamic")

    def __repr__(self):
        return self.name


class OrderDefault(BaseMixinsModel):
    """物料订单"""
    __tablename__ = "p_order_default"
    create_date = Column(DateTime(), default=datetime.now(), comment="添加时间")
    num = Column(Integer(), default=0, comment="数量")
    status = Column(Boolean(), default=True, comment="True进货，False出货")
    desc = Column(String(200), comment="描述")
    g_id = Column(Integer(), ForeignKey('p_goods_default.id'))
    goods = relationship("GoodsDefault", order_by='GoodsDefault.id', back_populates="OrderDefault")

    def __repr__(self):
        return self.desc
