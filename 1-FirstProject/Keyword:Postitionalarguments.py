def area(x, y):
    return x * y

print(area(4, 5))

def volume(x, y ,z):
    return x * y * z

print(volume(3, 4, 7))

# Keyword Arguments

def area(x, y):
    return x * y

print(area(x = 4,y =5)) 
# The X and Y assignment makes them keyword arguments. The alternative is called Positional arguments
# In keyword arguments the Position of the variables doesn't matter as they are assigned to each argument in order

def area(x, y = 2):
    return x * y

print(area(x = 4,y = 5 )) 

# This allows us to set Default parameter values. The Y Value is defaulted to a value of 2 but can be changed in the Argument Call.
# Default paramaters CANNOT be before non-default parameters******

#Arbitrary number of non-keyword arguments 

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 2, 3, 4, 5,))

# to create a def with unlimited args. Args can be any variable but args is good practice

# Arbitrary number of Keyword arguments

def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2 , c=3))

