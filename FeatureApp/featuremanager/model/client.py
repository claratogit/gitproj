# coding=utf-8
from sqlalchemy import Column, String, Integer

from featuremanager.model.base import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, name):
        self.name = name
 