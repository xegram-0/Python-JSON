# Exercise 1: Convert the following dictionary into JSON format
# data = {"key1" : "value1", "key2" : "value2"}

# Expected Output:

# data = {"key1" : "value1", "key2" : "value2"}

import json

data = {"key1" : "value1", "key2" : "value2"}
print(f"Converting {data} into JSON format...")
json_data = json.dumps(data)
print(json_data)