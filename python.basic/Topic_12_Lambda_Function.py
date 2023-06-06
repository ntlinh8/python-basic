# Lamda function is a small anonymous function
# Lamda function take any parameter, and one condition, though
# The format is 
# the store return value = lambda <parameters> : <condition>
# actually, the condition is a expression and it'll return a value, this value were stored in the x variable
# You can see the example:
x = lambda a: a*2
print(x(2))

# The lambda function with more than one parameter
x = lambda a, b, c, d : (a+b)*(d+c)
print(x(1,2,3,4))

# Actually, the lambda function get more value when it were used in the normal function
# if I have functions, them only differences from each orther by one parameter, 
# I'm going to write a format fuction using lambda function instead of define function
# Please, see the next example:
def multiple(n):
    return lambda a : a*n

# so if I need the duple and triple function, I don't need define it. 
# I'm going to call the multiple fucntion
# example
duple = multiple(2)
triple = multiple(3)

print(duple(10))
print(triple(10))
