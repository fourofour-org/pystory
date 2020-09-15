
# converting Python list to a dictionary 


books = ["The Alchemist", "Never split the difference" , 
    "The power of habit", "Industries of the Future", "The power of subconsious mind", "Antifragile"]

books_map = {}
for i in range(len(books)):
    books_map[books[i]] = i 

print(books_map) 