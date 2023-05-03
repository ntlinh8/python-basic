def ex1():
    n = int(input('Enter the value of n '))
    i = n
    while(i <= 100):
        if(i % 2 != 0):
            print(i)
        i += 1

def ex2():
    n = int(input('Enter the value of n '))
    i = 0
    while(i <= n):
        if(i % 3 == 0 and i % 7 == 0):
            print(i)
        i += 1

def ex3():
    sum = 0
    i = 0
    while(i <= 20):
        if(i % 2 == 0):
            print(i)
            sum += i
        i += 1
    print('Sum is ' + sum)

def ex4_1():
    n = int(input('Enter value of n '))
    if(22 <= n <= 65):
        print('Have a good work day')
    else:
        print('Be enjoy')

def ex4_2():
    n = int(input('Enter value of n '))
    age = 22
    isInRange = False
    while(age <= 65):
        if(age == n):
            isInRange = True
        age += 1
    print('Have a good work day' if isInRange else 'Be enjoy')
