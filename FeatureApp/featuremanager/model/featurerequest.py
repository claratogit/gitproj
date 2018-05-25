# coding=utf-8

from sqlalchemy import Column,ForeignKey, String, Integer, Date
from featuremanager.model.base import Base
from sqlalchemy.orm import relationship, backref
from client import Client
from productarea import ProductArea 

class FeatureRequest(Base):
    __tablename__ = 'featurerequests'
    # Here we define columns for the table FeatureRequest.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    description = Column(String(1000))
    client_id = Column(Integer, ForeignKey('clients.id'))
    targeted_date = Column(Date)
    productarea_id = Column(Integer, ForeignKey('productareas.id'))
    priority = Column(Integer)
    client = relationship(Client, backref=backref("featurerequests"))
    productarea = relationship(ProductArea, backref=backref("featurerequests"))
    
    def __init__(self, title, description, client, targeted_date, productarea, priority):
        self.title = title
        self.description = description
        self.client = client
        self.targeted_date = targeted_date
        self.productarea = productarea
        self.priority = priority