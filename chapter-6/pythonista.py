# Pythonista 

# how should we create a list of numbers from 1-100 
list_100_1 = []
for i in range(1, 101):
    list_100_1.append(i)

print(list_100_1)
# or 

list_100_2 = [*range(1,101)]
print(list_100_2)