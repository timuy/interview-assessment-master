from sqlalchemy import Column, String

from model.base import Base

class Coin(Base):

    __tablename__='COIN'
    
    id = Column(String(50),primary_key=True)
    name=Column(String(50))
    symbol = Column(String(50))
    
    def __init__(self,id,name,symbol):
        self.id = id
        self.name = name
        self.symbol = symbol
        
        