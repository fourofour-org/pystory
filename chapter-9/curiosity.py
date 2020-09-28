import math 
# accessing constants 
PI = math.pi
e = math.e 
inf = math.inf     # represents infinity , we can append a - sign to use a negative equivalent 
nan = math.nan    # represents a floating point not a number 

# ceiling and flooring a number 
num = 12.24
ceil_num = math.ceil(num)     # returns ceil value i.e. 13 as an integer
floor_num = math.floor(num)     # returns floor value i.e. 12 as an integer

# calculating factorial of a number 
num = 14 
num_fact = math.factorial(num)   # calculated 14 * 13 * 12 * . . . * 1 

# performing angular conversions 
# convert x degrees to radians 
x_degree = 90
x_rad = math.radians( x_degree )     # conversion from degree to radians 
# convert y radians to degrees
y_radians = math.pi / 2 
y_degrees = math.degrees( y_radians )     # convert PI / 2 radians to degrees 

# calculating common trigonometric functions 
x_degree = 90 
x_rad = math.radians( x_degree )
# calculate sin theta where theta is passed on as radians 
sin_x = math.sin( x_rad )
# calculate cos theta where theta is passed on as radians 
cos_x = math.cos( x_rad )
# calculate tan theta
tax_x = math.tan( x_rad )


# calculating logs and exponents 
x = 5 
# calculate e raised to power x , where e or math.e is a constant 2.718281 which is a base of natural logarithms
e_to_x = math.exp( x )
# calculate the natural log of x 
log_x = math.log( x ) 
# calculate log to the base 2 of x 
log_2_x = math.log2( x )
# calculate log to the base 10 of x 
log_10_x = math.log10( x ) 
# calculate y raised to power z
y = 25 
z =  2 
y_to_power_z = math.pow( y, z ) 
