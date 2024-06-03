# Exercise 8: Check whether following json is valid or invalid. If Invalid correct it

# { 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000
#             "bonus":800
#          }
#       }
#    }
# }

import json

def validateJson(data):
    try:
        json.loads(data)
    except ValueError as error:
        return "invalid"
    return "valid"

# The data must be in string ("""
#                               """)
json_data = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
"""
result = validateJson(json_data)
print(f"The json data is {result}")