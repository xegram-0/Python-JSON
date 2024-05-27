# Exercise 3: PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

# sampleJson = {"key1": "value1", "key2": "value2"}

# Expected Output:

# {
#   "key1" = "value2",
#   "key2" = "value2",
#   "key3" = "value3"
# }

import json

sampleJson = {"key1": "value1", "key2": "value2"}

# The samplejson is not a true json kind (with """""")
# thus resulting in error
#json_data = json.loads(sampleJson)

pretty_json = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(pretty_json)