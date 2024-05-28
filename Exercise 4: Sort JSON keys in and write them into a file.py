# Exercise 4: Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys

# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

# Expected Output:

# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }

import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

#pretty_json = json.dumps(sampleJson,indent=3,sort_keys=True)
#print(pretty_json)
# Without sort_key, the output would be:
# {
#    "id": 1,
#    "name": "value2",
#    "age": 29
# }

#print(type(pretty_json))
# Output: class: str
print("Beginning to write file...")
with open("json_to_pretty_sorted","w") as written_file:
    json.dump(sampleJson, written_file,indent=3,sort_keys=True)
    # Waring about dumps() and dump()
print("The end of writing file in JSON.")