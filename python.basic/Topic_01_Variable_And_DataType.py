# Knowledge
# In python, don't need declare a new variable. Only need assign to it a value, the variable will declared.abs
# Don't need to specify data type for variable. Python will use a value which was assigned to variable to set data type
# Eg: When we assign value is 5 to a. a is integer.
# 5.0 -> float
# 'S/W Engineering Part' -> str
# =====================
# We can specify tha data type for variable when assign by using casting
# eg: a = int(5)

# integer
a = 5
b = int(6)
print(a)
print(b)

# float
point = 5.6
average_point = float(9)
print(point)

# complex
x = 1 - 4j
y = 34 + 5j
print(x + y)


# string
name = 'Elon Musk'
email_address = ' No. 1, Pham Van Bach Street, Cau Giay District, Ha Noi, Viet Nam'
print('{} is living in {}'.format(name, email_address))

#There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# list
fruit_list = ['banana', 'apple', 'cherry']
print(fruit_list[2])

# tuple
# Tuple items are ordered, unchangeable, and allow duplicate values.
fruit_tuple = ('banana', 'apple', 'cherry')
print(fruit_tuple[1] + ' ' + fruit_list[0] + 'are my favorite food')
# Tuple items can be of any data type:
name_tuple = ('Linh', 'Lan', 'Phuong')
name_tuple_with_one_item = ('Linh',) # need , charactor
# A tuple can contain different data types:
infor_user_1 = ('An', 'Nguyen Van', 42342, 5.6, 6.9, 7.0, True)
