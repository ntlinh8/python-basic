def ex1():
    n = int(input('Enter value of n: '))
    for i in range(n):
        print(i)

def ex1_1():
    n = int(input('Enter value of n '))
    for i in range(n, -1, -1):
        print(i)

def ex2():
    a = int(input('Enter value of a '))
    b = int(input('Enter value of b '))
    for i in range(a, b+1):
        print(i)

def ex3():
    a = int(input('Enter value of a '))
    b = int(input('Enter value of b '))
    sum = 0
    for i in range(a, b+1):
        if i%2 == 0:
            sum += i
            print(i)
    print(sum)

def ex4():
    a = int(input('Enter value of a '))
    b = int(input('Enter value of b '))
    for i in range(a, b+1):
        if i%3 == 0:
            print(i)

def ex5():
    n = int(input('Enter value of n '))
    result = 1
    for i in range(a, b+1):
        result *= i
    print(result)

def ex6():
    backet = ['banana', 'watermelon', 'apple', 'orange', 'cherry', 'strawberry']
    isExist = False
    for item in backet:
        if(item == 'orange'):
            isExist = True
    print(isExist)