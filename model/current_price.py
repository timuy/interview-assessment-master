from sqlalchemy import Column, Float, DateTime,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

from model.base import Base


class CurrentPrice(Base):

    __tablename__='CURRENT_PRICE'
    id = Column(Integer,primary_key=True)
    coin_id = Column(String(50),ForeignKey('COIN.id'))
    coin = relationship("Coin",uselist=False)
    current_price = Column(Float)
    date_searched = Column(DateTime)
    
    def __init__(self,coin,current_price,date_searched):
        self.coin = coin
        self.current_price = current_price
        self.date_searched = date_searched
        
        