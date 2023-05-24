# Before leaning the collection data type, we need discern List, Tuple, Dictionary, Set, Frozen Set
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# the tuple is an encapsulation structure -> cannot change the value of tuple (changing is override)
# the list is a fluent structure (can remove, add, override)

##################### List #####################
fruit_list = ['apple', 'banana', 'cherry', 'watermelon', 'brocolli', 'orange', 'strawberry', 'avocado', 'dragon fruit']

# list access the duplicate item and items with the difference data type
list_1 = ['banana', 1, True, 5.33, 'banana']
print('Print all items in list_1: ' + list_1)

# get the item/sublist in list by index
print('Print item with index 1 in fruit_list: ' + fruit_list[1])
print('Print item with index -1 in fruit_list: ' + fruit_list[-1])
print('Sublist trong fruit_list from index 2 to 5: ' , fruit_list[2:5])
print('Sublist trong fruit_list from index 0 to 2: ' , fruit_list[:2])
print('Sublist trong fruit_list from index 3: ' , fruit_list[3:])
print('Check item exist in fruit_list: ' , 'apple' in fruit_list)
print('Check item exist in fruit_list: ' , 'kiwi' in fruit_list)

# change/override the value of item in list
fruit_list[2] = 'kiwi'
print('Print fruit_list after override item have index 2: ', fruit_list)

fruit_list[2:4] = ['banini', 'kiwimelon']
print('Print fruit_list after override sublist[2-4]: ', fruit_list)

# insert the new item to the list by index (without override any of existing value)
fruit_list.insert(4, 'cherrylady')
print('Print fruit_list after insert new item to the index 4', fruit_list)

# insert the new item to the last position of the list
fruit_list.append('mango')
print('Print fruit_list after add new item to the last position', fruit_list)

# insert many items to the last position of the list (many items can in the another list)
tropical = ['pineapple', 'papaya']
fruit_list.extend(tropical)
print('Print fruit_list after add the items in tropical list: ', fruit_list)

# in addition, we can insert many items to the list position of the list (many items exist in the set/tuple/dictitionary)
tropical_set = {'pineapple_set', 'papaya_set'}
tropical_tuple = ('pineapple_tuple', 'papaya_tuple')
tropical_dict = {'fruit_1':'pineapple_dict', 'fruit_2':'papaya_dict'}

fruit_list.extend(tropical_set)
print('Print fruit_list after add the items in tropical set: ', fruit_list)
fruit_list.extend(tropical_tuple)
print('Print fruit_list after add the items in tropical tuple: ', fruit_list)
fruit_list.extend(tropical_dict)
print('Print fruit_list after add the items in tropical dict: ', fruit_list)

# Remove List Items
# 1. Remove List Items by value of item
fruit_list.remove('fruit_1')
print('Print fruit_list after remove fruit_1 item ', fruit_list)

# 2. Remove List Items by index of item
fruit_list.pop(-1)
fruit_list.pop(len(fruit_list)-1)
fruit_list.pop(2)
print('Print fruit_list after remove items in index -1, len and 2 ', fruit_list)

# Note: if you use the pop function with empty parameter, the last item in the list will be removed
fruit_list.pop()
print('Print fruit_list after remove the last item', fruit_list)

# In addition, we have another way to remove item from the list, 
# but the way only remove item by index or remove all item in the list and remove this list
del fruit_list[-1]
print('Print fruit_list after remove the last item', fruit_list)

del tropical
# print('Print tropical after remove this list', tropical) 
#so, this statement will throw an exception because tropical wasn't define

# if you want to remove/delete all item in the list (without delete the list)
# you can use the clear function like that
fruit_list.clear()
print('Print fruit_list after it was cleared', fruit_list)

# sort list with sort method, the list will sort the list alpha, ascending 
fruit_list = ['watermelon', 'apple', 'banana', 'cherry',]
fruit_list.sort()
print('Print fruit_list after it was sorted', fruit_list)

# if you want to sort descending, 
# way 1: you can change the default argument of sort method (set the reverse = True)
fruit_list.sort(reverse = True)
print('Print fruit_list after it was sorted descending', fruit_list)

# way 2: using 2 methods by sequence: sort > reverse
fruit_list.sort()
fruit_list.reverse()
print('Print fruit_list after it was sorted descending', fruit_list)

# customize sort
# if you want to sort by another value (withou the value of item)
# abs is absolute value calculate method
def DistanceWith50(n):
    return abs(50-n)

number_list = [12, 4, 52, 49, 25, 77, 100]
number_list.sort(key = DistanceWith50)
print('Print number_list after sort by the distance with 50: number_list = ', number_list)

# sensitive with sort method
# in default the sort mothod will sort with sensitive mode
# so, if you want to ignore the sensitive charactor, you can using convert all item to lower case or upper case
# this way like the previous way (using customize sort) because uppercase() and lowercase() also methods
# the difference's only the define position of method. Uppercase() and lowercase() is method of string class
upper_lowser_list = ['Hello', 'this', 'Is', 'Brian', 'calling']
upper_lowser_list.sort(key = str.upper)
print('Print upper_lowser_list after sort by upper case: upper_lowser_list = ', upper_lowser_list)
upper_lowser_list.sort(key = str.lower)
print('Print upper_lowser_list after sort by lower case: upper_lowser_list = ', upper_lowser_list)

# Reverse method
# reverse the list, this method can mix with sort method
fruit_list.reverse()
print('Print fruit_list after it was sorted descending', fruit_list)

# To avoid the reference to the memory area, when assign the list a for list b, 
# we need to use copy or declare again list
# Stop using list_A = list_B
# We need to use 
list_A = fruit_list.copy()
list_B = list(fruit_list)
print('Print list_A: ', list_A)
print('Print memory of list_A: ', id(list_A))
print('Print memory of fruit_list: ', id(fruit_list))

# Join list
# way 1: using + operator
print('Print list_A join list_C using plus operator: ', list_A + list_B)

# way 2: using append
for item in list_B:
    list_A.append(item)
print('Print list_A join list_C using plus append: ', list_A)

# way 3: using extend
list_A.extend(list_B)
print('Print list_A join list_C using plus extend: ', list_A)

# list with loop statement
# with for loop, there are 2 way to get all value in the list

# way 1: for in list
for item in list_A:
    print(item)

# way 2: for in range
for i in range (len(list_A)-1):
    print(list_A[i])

# with while loop, you can see that:
i = 0
while i < len(list_A):
  print(list_A[i])
  i = i + 1

# A short hand for loop, but this way is NOT recommended
[print(item) for item in list_A]

# list comprehension
# there are so many way to write with short hand
# this statement meaning is get all items in fruit_list that contains a charactor
newlist = [x for x in fruit_list if "a" in x]
# the syntax is newlist = [expression for item in iterable if condition == True]

##################### Tuple #####################
# Tuple is a data type that is used to store collections of data
# a tuple is a collection which is ordered and unchangeable
# Tuple items are ordered, unchangeable, and allow duplicate values.
fruit_tuple = ('banana', 'apple', 'cherry')

# with a tuple with only one item, we need define like that:
tuple_1 = ('banana',)

# tuple access the duplicate item and items with the difference data type
tuple_1 = ('banana', 1, True, 5.33, 'banana')

# because the tuple is order, so we can get the item in the tuple by index
print('Print the item in tuple by index 1: ', fruit_tuple[1])
print('Print the item in tuple by index -1: ', fruit_tuple[-1])
print('Print the item in tuple by index 1-2: ', fruit_tuple[1:2])
print('Print the item in tuple by index from 0 to 2: ', fruit_tuple[:2])
print('Print the item in tuple by index from 3: ', fruit_tuple[2])

# Get length of tuple
print('Print the length of tuple: ', len(fruit_tuple))

# Even so, we cannot to change the order of tuple
# NO change is meaning NO override and NO sort (change value of item and change index of item)
# so above statement will throw an exception, tuple does not support assign operator (no changed)
# fruit_tuple[2] = 'kiwi'

# Check item exist in tuple
print('Check item exist in tuple', 'apple' in fruit_tuple)

# Because tuple is a collection which no changed. So, if you want to update the tuple (add, remove, replace), 
# we need to convert tuple to list -> update -> convert to tuple again
fruit_list = list(fruit_tuple)
fruit_list.append('mango')
fruit_list = tuple(fruit_list)

# unpack tuple
# we can unpack tuple by 2 ways like that
# way 1: using the single variable
tuple_2 = ('hoa', 'hue', 'lan', 'phuong', 'quan')
(name_1, name_2, name_3, name_4, name_5) = tuple_2
print('Value of name_1: ', name_1)
print('Value of name_2: ', name_2)
print('Value of name_3: ', name_3)
print('Value of name_4: ', name_4)
print('Value of name_5: ', name_5)

# way 2: you can using rest parameter
(name_1, name_2, *name_3) = tuple_2
print('Value of name_1 using rest parameter: ', name_1)
print('Value of name_2 using rest parameter: ', name_2)
print('Value of name_3 using rest parameter: ', name_3)

# Loop statement with tuple data type like the list
for item in fruit_tuple:
    print(item)

# if you wan to update the tuple, you only convert it to list and update
# in addition this way, with join tuple situation, we can join 2 tuple using plus operator or multiple operator

print('Tuple 1 + tuple 2 ', tuple_1 + tuple_2)
print('Tuple 1 * index ', tuple_1 * 2)




