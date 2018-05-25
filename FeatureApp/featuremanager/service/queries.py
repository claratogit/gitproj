# coding=utf-8
import sys
sys.path.append('/home/user1/Workspace/FeatureApp/')

import json
import datetime

from json import dumps
from sqlalchemy.orm import class_mapper
# 1 - imports
from featuremanager.model.client import Client
from featuremanager.model.productarea import ProductArea
from featuremanager.model.featurerequest import FeatureRequest
from featuremanager.model.base import Session


def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()

class DataRetriever:
    
    session = Session()

    def getAllClients(self):
        # 3 - extract all movies
        # clients = self.session.query(Client).all()
        serialized_labels = [
            dataretriever.serialize(label)
            for label in self.session.query(Client).all()
        ]        
        return dumps(serialized_labels)
    
    def getAllProductAreas(self):
        # 3 - extract all movies
        serialized_labels = [
            dataretriever.serialize(label)
            for label in self.session.query(ProductArea).all()
        ]        
        return dumps(serialized_labels)

    def getAllFeatureRequests(self):
        # featureReqs = self.session.query(FeatureRequest).all()
        # return featureReqs
        serialized_labels = [
            dataretriever.serialize(label)
            for label in self.session.query(FeatureRequest).all()
        ]        
        return dumps(serialized_labels, default = myconverter)
    
    def getAllClientFeaturerequests(self, clientName):
        # featureReqs = self.session.query(FeatureRequest).join(Client, FeatureRequest.client).filter(Client.name == clientName).all()
        # return featureReqs
        serialized_labels = [
            dataretriever.serialize(label)
            for label in self.session.query(FeatureRequest).join(Client, FeatureRequest.client).filter(Client.name == clientName).all()
        ]        
        return dumps(serialized_labels, default = myconverter)

    def serialize(self, model):
        """Transforms a model into a dictionary which can be dumped to JSON."""
        # first we get the names of all the columns on your model
        columns = [c.key for c in class_mapper(model.__class__).columns]
        # then we return their values in a dict
        return dict((c, getattr(model, c)) for c in columns)
    


dataretriever = DataRetriever()

allclients = dataretriever.getAllClients()
print(allclients)
# for tmpclient in allclients:
#     print(tmpclient.name)

pas = dataretriever.getAllProductAreas()
print(pas)
# for tmppas in pas:
#     print(tmppas.name)

freqs = dataretriever.getAllFeatureRequests()
print(freqs)
# for tmpfr in freqs:
#     print(tmpfr.title,  tmpfr.description,tmpfr.client.name ,tmpfr.productarea.name, tmpfr.priority)

print("\n\nClient sprcific feature requests --- ")
freqs = dataretriever.getAllClientFeaturerequests("Client 1")
print(freqs)
# for tmpfr in freqs:
#     print(tmpfr.title,  tmpfr.description,tmpfr.client.name ,tmpfr.productarea.name, tmpfr.priority)


# print(allclients)
# # 4 - print movies' details
# print('\n### All Feature :')
# for featureReq in featureReqs:
#     print(featureReq.title, featureReq.description, featureReq.client.name, featureReq.productarea.name)
# print('')

# for featureReq in featureReqs:
#     print(featureReq.title, featureReq.description, featureReq.client.name, featureReq.productarea.name)
# print('')

