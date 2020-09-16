# Monotonous Life 


![Monotonous][logo]

[logo]: monotonous.jpg "Monotonous Life"

## Monotonous Life is not always to be considered a negative  

> Programs which are running in the nano world, even they are happy because of the belief that their lives are not monotonous and the evil ones know that someday some user will give them the inputs they need to mess with the CPU time and memory space and then their are good ones who know that they'll find a code who'll help them to use CPU and Memory as wisely as possible. Yes as mentioned in the first chapter itself, there are some secrets of the nano world where the battle is all about time and space.  

> Point has a way of thinking which makes him to think of the programs as living creatures. Just like living creatures have their own fights in ilfe, so is the case with program at the nano world. 

> Point visualises them to be living creatures, who live on the hard drive but upon call of duty, they've to leave their house or at least a copy of theirs has to leave the house and go to the main memory and do what they are meant to do. As per Point they've a life too. And once they've served their purpose, a time comes when they're deleted forever.  

> The story of nano world is fascinating and we'll be talking more about it in each episode. 


> Meanwhile in India, it's another day in monotonous life of Point. Point loved the dictionaries after they helped him to organise his books in an order. Now he's doing some more experiments using the dictionaries. 

And beacuse you're here to help him and you're good with dictionary comprehensions, you're going to use your skills and help Point. 

## General way to implement dictionary comprehensions 
```
new_d = { k:v for (k,v) in d.items() }

```

Yes it means you can access all the key / value pairs in a dictionary using the d.items method. 

What do you think could be some of the usecases for a dict comprehension? 

1. How about swapping key-values ? 

```
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

```



[Monotonous Life](monotonous.py)