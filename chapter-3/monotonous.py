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

print(new_d)