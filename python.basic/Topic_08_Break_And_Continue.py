def ex1():
    n = int(input('Enter value of n '))
    isExist = False 
    for i in range(1, n+1):
        if(i % 3 == 0):
            print(i)
            isExist = True
            break
    print('Ton tai so chia het cho 3' if isExist else 'Khong ton tai so chia het cho 3')

def ex2():
    a = int(input('Enter value of a '))
    b = int(input('Enter value of b '))
    for i in range(a, b):
        if(i%2 == 0):
            continue
        print(i)



