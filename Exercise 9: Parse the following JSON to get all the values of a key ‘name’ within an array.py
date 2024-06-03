# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array


# [ 
#    { 
#       "id":1,
#       "name":"name1",
#       "color":[ 
#          "red",
#          "green"
#       ]
#    },
#    { 
#       "id":2,
#       "name":"name2",
#       "color":[ 
#          "pink",
#          "yellow"
#       ]
#    }
# ]
# Expected Output:

# ["name1", "name2"]


import json 

json_data = """
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
"""


the_data = json.loads(json_data)
targetData = [item.get("name") for item in the_data]
print(targetData)