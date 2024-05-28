# Exercise 5: Access the nested key ‘salary’ from the following JSONimport json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# # write code to print the value of salary

# Expected Output:

# 7000

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
json_data = json.loads(sampleJson)
#print(json_data)
# You cannnot do the following with the raw json data
# but have to convert it to python data then access it
# via list element
print(json_data["company"]["employee"]["payble"]["salary"])