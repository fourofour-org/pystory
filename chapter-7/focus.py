import time
start = time.time()

# do some processing 

end = time.time()

total_time = end - start 

print("Time elapsed:" + str(total_time)) 
# conversion to str because total_time is a float