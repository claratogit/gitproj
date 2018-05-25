# coding=utf-8

# 1 - imports
import sys
sys.path.append('/home/user1/Workspace/FeatureApp/')

print("Initialize DB")

from datetime import date

from featuremanager.model.client import Client
from featuremanager.model.base import Session, engine, Base
from featuremanager.model.productarea import ProductArea
from featuremanager.model.featurerequest import FeatureRequest

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create clients
client1 = Client("Client 1")
client2 = Client("Client 2")
client3 = Client("Client 3")

# 5 - creates product areas
productarea1 = ProductArea("Area ABC")
productarea2 = ProductArea("Area XYZ")

# 6 - add feature request details
featurerequest1 = FeatureRequest("Feature 1 for Cl 1", "Add a menu for feature 1", client1, date(2018, 5, 2), productarea1, 1)
featurerequest2 = FeatureRequest("Feature 1 for Cl 2", "Add a menu for feature 1", client2, date(2018, 5, 12), productarea1, 1)
featurerequest3 = FeatureRequest("Feature 2 for Cl 1", "Add a submenu for feature 1", client1, date(2018, 5, 5), productarea1, 2)

# 7 - persists data
session.add(client1)
session.add(client2)
session.add(client3)

session.add(productarea1)
session.add(productarea2)

session.add(featurerequest1)
session.add(featurerequest2)
session.add(featurerequest3)

# 10 - commit and close session
session.commit()
session.close()