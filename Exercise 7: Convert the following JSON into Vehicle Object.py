# Exercise 7: Convert the following JSON into Vehicle Object
# { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }

# For example, we should be able to access Vehicle Object using the dot operator like this.

# vehicleObj.name, vehicleObj.engine, vehicleObj.price

import json

# This one requires to be str not this!!!

# from json import JSONEncoder
# from collections import namedtuple

# def customVehicleClass(VehicleDict):
#     return namedtuple('X',VehicleDict.keys()(*VehicleDict.values()))

# json_data = { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }

# vehicleObj = json.loads(json_data,object_hook=customVehicleClass)

# print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.price = price
        self.engine = engine

# This function works as a translator
def customVehicleClass(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

# This has to be a string
vehicle_data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

vehicleObj = json.loads(vehicle_data, object_hook=customVehicleClass)

print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)