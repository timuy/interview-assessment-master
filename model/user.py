from sqlalchemy import Column, String,Integer

from model.base import Base


class User(Base):

    __tablename__='USER'
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50))
    email_address = Column(String(50))
    
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        
        