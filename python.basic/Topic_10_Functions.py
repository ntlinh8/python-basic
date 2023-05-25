# Python syntax is pretty easy. You can see a simple function like that:
from cgitb import reset


def my_func():
    print('Hello, world!')

# The function can have one or more parameter and return result
# You can define the number of parameter in the define process
# this is a function with one parameter
def hello_name(name):
    print('Hey dude, your name is', name , 'right?')

# When we need to use the function like:
# Because with python, we cannot to define data type for the parameter
name1 = 'Linh'
name2 = 123
name3 = ['Linh', 'Lan', 'Phuong']
name4 = ('banana', 'cherry', 'apple')
name5 = 123.11
hello_name(name1)
hello_name(name2)
hello_name(name3)
hello_name(name4)
hello_name(name5)

# This is a function with 2 parameters
def print_user_information(name, company):
    print('Hi, this is', name, 'from', company)

print_user_information('Linh', 'Samsung SDS VietNam')
print_user_information('Bob', 'school')

# So if you don't know the number of argument that we will get to the function
# we can using rest paramenter with *arg
# example 1
left_menu_locator = "//div[text()='{}']"
user_information_row_text = "//div[text()='{}']/../..//span[text()='{}']"
def get_dynamic_locator(dynamic_locator, *value):
    return str(dynamic_locator).format(*value)

print(get_dynamic_locator(left_menu_locator, 'Customer'))
print(get_dynamic_locator(user_information_row_text, 'Nguyen Van An', 'annguyenvan@gmail.com'))

# example 1
def employee_in_department(department_name, *user_list):
    print('In this', department_name, 'department, there are some employee: ')
    for user_list in user_list:
        print('UserName is ', user_list['UserName'])
        print('Email is ', user_list['Email'])
        print('Year of birth is ', user_list['Year Of Birth'])
        

User_1 = {
    'UserName' : 'Bob Jackson',
    'Email' : 'bobjackson@gmail.com',
    'Year Of Birth' : 1994
}

User_2 = {
    'UserName' : 'Brian Kennedy',
    'Email' : 'briankennedy@gmail.com',
    'Year Of Birth' : 1995
}
employee_in_department('S/W Engineering Part', User_1, User_2)

# Typically, the passed arguments will have to be arranged in the correct order of the parameters
# But if you don't want to arranging, you can define it like a dictionary

def my_child(child1, child2, child3):
    print(child1, 'is the first child')
    print(child2, 'is the second child')
    print(child3, 'is the third child')

my_child('Anna', 'Bob', 'Emy')
my_child(child2 = 'Anna', child3 = 'Bob', child1 = 'Emy')

# Rest Parameter with keyword argunemt, we can using with **arg
def print_last_name(**kid):
  print("His last name is " + kid["lname"])

print_last_name(fname = "Tobias", lname = "Refsnes") 

# We can define a parameter with default value
def hover_to_element(locator, timeout = 2):
    print('Hover to the', locator, 'element in', timeout, 'seconds')

hover_to_element('button#registor')
hover_to_element('button#registor', 5)

# Define a function with return value
def calculate_sum(*value):
    result = 0
    for item in value:
        result += item
    return result

print('Sum is', calculate_sum(1,2,4,5))
print('Sum is', calculate_sum(1,2))

# With the function which will be overrided in the subclass
# But we don't need to action in this function (subclass)
# But in python, when the function was defined, the statement is required
# We cannot to define a function with no statement
# so, to soulve this problem, the pass statement was created
# the pass statement is a statement with no action
def function_was_overrided():
    pass

# recursion with python
# Required: Calculate multiple of the number which less more n
# Eg: n = 5, return 5*4*3*2*1
def calculate(n):
    if n == 1:
        return 1
    else:
        return n*calculate(n-1)

print('Calculate multiple of the number which less more 5 is', calculate(5))
