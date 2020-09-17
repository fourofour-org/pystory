#Let's say there's an ID associated with each unique name of an appliance in an IOT project. 
d = {
    "kitchen_bulb": "1245",
    "living_room_fan": "1246",
    "bed_room_ac": "1255",
    "robo_assistant": "1333",
    "microwave": "1267"
}

#Now let's say we have an ID and we want to check which appliance it associates with. 

new_d = { v:k for (k,v) in d.items() }

# print(new_d)

# muliply all the values of a dict by 2 

single = {
    "a": 1,
    "b": 2,
    "c": 3
}

double = { k: v*2 for (k,v) in single.items()}

print(double)

# let's add in some conditions , only double if v % 2 == 0 

even_double = { k: v*2 for (k,v) in single.items() if v%2 ==0}

print(even_double)