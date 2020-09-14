# Point's shopping script 

# Python's way of printing to screen 
print("It's a good sunny day! Let's visit market")

items_to_buy = ["milk", "bread", "cheese", "almonds", "bananas"]
money = 200 
print("All set to go to the market")
cart = [] 

import time 
start_time = time.time() 

# get the first item from the items_to_buy
target_item = items_to_buy.pop()

# add milk to cart 
cart.append("milk")

# cost of milk = 10 
# remaining money 
money = money - 10 

# next item to buy 
target_item = items_to_buy.pop() 
print(target_item)


# add bread to cart 
cart.append("bread")

# cost of bread = 20 
money = money - 20 

# next item to buy 
target_item = items_to_buy.pop() 
print(target_item)

# add cheese to cart 
cart.append("cheese")

# cost of cheese = 40 
money = money - 40 

# next item to buy 
target_item = items_to_buy.pop() 
print(target_item)

end_time = time.time()

total_time = end_time - start_time 

print(total_time)