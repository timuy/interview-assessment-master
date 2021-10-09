from sqlalchemy import Column, Float, DateTime, Integer,String,ForeignKey
from sqlalchemy.orm import relationship

from model.base import Base

class Order(Base):

    __tablename__='ORDER'

    id = Column(Integer,primary_key=True, autoincrement=True)
    user_id = Column(Integer,ForeignKey('USER.id'))
    user = relationship("User",uselist=False)    
    coin_id = Column(String(50),ForeignKey('COIN.id'))
    coin = relationship("Coin",uselist=False)
    purchase_price = Column(Float)
    date_purchased = Column(DateTime)
    quantity = Column(Integer)
    
    def __init__(self,user,coin,purchase_price,date_purchased,quantity):
        self.user = user
        self.coin = coin
        self.purchase_price = purchase_price
        self.date_purchased = date_purchased
        self.quantity = quantity
        
        