# The Beginning 


![Time and  Space][logo]

[logo]: time-and-space.png "Time and Space"

## It is a battle of time and space 

> It is a battle which is happening on a nano scale. Where 
weird beings called programs are fighting for CPU time and 
memory space. 

> I know it sounds interesting, but this is just the first 
episode and we're in no hurry to reveal the secrets of the 
world which lies in time and space. 

> Meanwhile in India, there lives a programmer who's trying 
to grasp data structures and algorithms and machine learning 
and hardware and essentially everything about the journey of 
an electron from sand to satellites. 

> The name of the programmer is **Point**  

Yeah the story is interesting for sure, but you're here not 
only to hear Point's story but also to help him with his 
daily life. And while trying to help him, you're going to 
learn some good things about this language called **Python** 


Episode-1 *Point goes to the market* 

**Plot:** Point is going to market and so he creates a list of 
items he needs to buy, he mostly thinks and talks Python. 

```

print("It's a good sunny day! Let's visit market")

items_to_buy = ["milk', "bread", "cheese", "almonds", "bananas"]
money = 200 
print("All set to go to the market")
cart = [] 

```

**Point** starts walking towards the market and checks time and 
decides the first item to buy 

```
import time 
start_time = time.time() 

# get the first item from the items_to_buy
target_item = items_to_buy.pop()

```

**Point** reaches milk shop and purchases milk 

```

# add milk to cart 
cart.append("milk")

# cost of milk = 10 
# remaining money 
money = money - 10 

# next item to buy 
target_item = items_to_buy.pop() 
print(target_item)

```

**Point** point reaches bread shop 

```
# add bread to cart 
cart.append("bread")

# cost of bread = 20 
money = money - 20 

# next item to buy 
target_item = items_to_buy.pop() 
print(target_item)
``` 

**Point** point reaches cheese shop 


```
# add cheese to cart 
cart.append("cheese")

# cost of cheese = 40 
money = money - 40 

# next item to buy 
target_item = items_to_buy.pop() 
print(target_item)
``` 

Yeah by now, you know how point's gonna buy the remaining items.
And finally when the shopping is done. Point reaches back home 
and checks how long the shopping took. 

```

end_time = time.time()

total_time = end_time - start_time 

print(total_time)

```


Point thinks that he's taking too long for shopping and needs 
to optimise on a few things in terms of his habits. He plans on 
to adopt good habits. 

> What he does next? 

That's for the next episode of pystory !! 

## Complete Code for this episode 

[Point's Breakfast Shopping](points-shopping.py)
