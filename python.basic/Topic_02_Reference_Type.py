# In python, all data type is reference type
list_a = ['banana', 'apple', 'cherry']
list_b = list_a
list_a[0] = 'water melon'
print(list_a)
print(list_b)
# list_a = ['water melon', 'apple', 'cherry']
# list_b = ['water melon', 'apple', 'cherry']
#=============================
a = 5        # a variable is reference to the storage area, the storage contains a value that is 5
b = a        # b variable is reference to the storage area of a
a = 7       # declare and assign for a variable to the storage area, it contains value is 7
print(a)
print(b)
# a = 7
# b = 5

#=============================
# To avoid this, when we want to copy the value of variable a to variable b
# we need to declare a new variable b. 
# Give it a reference to the new memory area 
# and copy the value of the variable a into that memory area
list_a = ['banana', 'apple', 'cherry']
list_b = list(list_a) # declare and assign value for b variable
list_a[0] = 'water melon'
print(list_a)
print(list_b)
# list_a = ['water melon', 'apple', 'cherry']
# list_b = ['banana', 'apple', 'cherry']
