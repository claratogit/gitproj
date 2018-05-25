# coding=utf-8

from sqlalchemy import Column, String, Integer

from featuremanager.model.base import Base

class ProductArea(Base):
    __tablename__ = 'productareas'
    # Here we define columns for the table ProductArea
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, name):
        self.name = name
