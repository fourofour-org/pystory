# Get Organised 


![Get Organised][logo]

[logo]: get-organised.jpg "Get Organised"

## Organisation is an important aspect  

> Programs which are running in the nano world are always hopoing for the warriors who help them move from one place to another. Their destiny is in the hands which provide them the necessary electronic forces which moves them. 

> Different programs have different roles at the nano scale. ps is a program whose job is to observe at nano scale who is sitting in the CPU and to push the information bytes to screen

> It's one of the dreams of any program to send their bytes to screen or receive some bytes of information from screen. 

> The story of nano world is fascinating and we'll be talking more about it in each episode. 


> Meanwhile in India, it's a usual day in Point's life. He has a organised his books in a sequence. But he doesn't want to invest time in searching for a specific title. He just wants to know where the book is as soon as he names it. 

Now as you know, you're here to help **Point** live a comfortable life. Let's see what you can do for him. 


## How about converting list to a dictionary with list values as keys and indexes as values. 

books = ["The Alchemist", "Never split the difference" , 
    "The power of habit", "Industries of the Future", "The power of subconsious mind", "Antifragile"]

**Let's try to convert this to a dictionary** 

```
books = ["The Alchemist", "Never split the difference" , 
    "The power of habit", "Industries of the Future", "The power of subconsious mind", "Antifragile"]

books_map = {}
for i in range(len(books)):
    books_map[books[i]] = i 

print(books_map) 

``` 

[Code for Get Organised](get-organised.py)