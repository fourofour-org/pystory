

# tuples are python's inbuilt containers which are 
# immutable 
# Python as a language has a taste for organisation 
# Nobody punishes you for not being organised as much as 
# Python 

import sys # for system related variables / operations 

# let's organise data in a tuple 
# name, language, years of experience
programmer1 = 'Nj', 'Nodejs', 12

print(type(programmer1))

years_of_experience = programmer1[2] # tuples support indexes only for reads 

# notice the 4 spaces. It's pythonic way of distinguishing 
# between different blocks of code 

if ( years_of_experience > 10 ): 
    print('a native programmer')
else:
    print('a naive programmer')

print(sys.getsizeof(programmer1))
# prints 80 on mac os catalina python 3.7.6 
programmer2 = ()
print(sys.getsizeof(programmer2)) 
# prints 56 

# Compare with a list 
programmer3 = [] 
print(sys.getsizeof(programmer3))
# prints 72  

# Compare with an int 
p4 = 4 
print(sys.getsizeof(p4))
# prints 28 


# Confusing ? 

'''
Yes there are certain confusions but they can be cleared. 
so all that we have to do is to declare a new tuple with 
less or more number of elements and check its size
'''

# using strings 
t1 = ('one',)
print(sys.getsizeof(t1))
# 64
t2 = ()
print(sys.getsizeof(t2))
# 56 
t3 = ('one', 'two', 'three', 'four')
print(sys.getsizeof(t3))
# 88 

'''
There is an interesting observation here, it is that the 
base size of tuple is 56 and with each new element which is 
getting added, the size grows by 8 bytes 
'''  

'''
One last thing to observe is whether this size is constant 
irrespective of size type of the element 
''' 

t4 = ('one', 'twooooooooooooooooooooooooooooooooooooooo')
print(sys.getsizeof(t4))
# 72 = 56 + 8 + 8 
'''
    Is it safe to conclude , that tuple is only storing 
    references ? 
    We really don't know but discover as this journey 
    continues 
''' 