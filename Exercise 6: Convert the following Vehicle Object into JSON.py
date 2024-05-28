# Exercise 6: Convert the following Vehicle Object into JSON
# import json

# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# # Convert it into JSON format

# Expected Output:

# {
#     "name": "Toyota Rav4",
#     "engine": "2.5L",
#     "price": 32000
# }

import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

obj_to_json = [f"{vehicle.name},{vehicle.engine},{vehicle.price}"]
#print(obj_to_json)
json_data = json.dumps(obj_to_json,indent=4,cls=)
print(json_data)

