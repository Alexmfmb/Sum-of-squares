import math
def Is_Square(num):
    if num == 0: return False

    root = math.sqrt(num)

    square = int(root + 0.5)**2

    if square == num:
        return True
    else:
        return False

def next_smaller_square(num):
    if num == 1 : return 0

    a = 0
    for i in range(num):
        if Is_Square(i):
            a = i

    return a

def Sum_of_two(num):
    start = num
    while start != 0:
        a = next_smaller_square(start)
        if a == 0: 
            return(False,0,0)

        b = num - a 

        if Is_Square(b):
            roota = math.sqrt(a)
            rootb = math.sqrt(b)
            return(True, roota, rootb)
        else:
            start = a

    return (False, 0 , 0)

def Sum_of_three(num):
    start = num
    while start != 0:
        a = next_smaller_square(start)
        if a == 0:
            return (False,0,0,0)
        
        b = num - a 
        testauf2 = Sum_of_two(b)

        if testauf2[0]:
            roota = math.sqrt(a)
            return(True,roota,testauf2[1],testauf2[2])
        else:
            start = a
    return (False,0,0,0)

def Sum_of_four(num):
    start = num
    while start != 0:
        a = next_smaller_square(start)
        if a == 0: 
            return (False,0,0,0,0)
        
        b = num - a 
        testauf3 = Sum_of_three(b)

        if testauf3[0]:
            roota = math.sqrt(a)
            return(True,roota,testauf3[1],testauf3[2],testauf3[3])
        else:
            start = a
    return (False,0,0,0,0)

def Sum_of_five(num):
    start = num
    while start != 0:
        a = next_smaller_square(start)
        if a == 0: 
            return (False,0,0,0,0,0)
        
        b = num - a 
        testauf4 = Sum_of_four(b)

        if testauf4[0]:
            roota = math.sqrt(a)
            return(True,roota,testauf4[1],testauf4[2],testauf4[3],testauf4[4])
        else:
            start = a
    return (False,0,0,0,0,0)

def Sum_of_n(num,n):
    start = num
    while start != 0:
        a = next_smaller_square(start)
        if a == 0:  #if next smaller square of a is 0, then a is 1, therefore the loop ends
            return [False] + n * [0]
        
        b = num - a 
        sum_of_n_minus_one = Sum_of_n(b,n - 1)

        if sum_of_n_minus_one[0]:
            roota = math.sqrt(a)
            stuff = [sum_of_n_minus_one[i] for i in range(1, n - 1 )]
            return [True,roota] + stuff
        else:
            start = a
            
    return [False] + n * [0]



if __name__ == '__main__':
    inp = input("A positive Integer:")
    num = int(inp)
    two_data = Sum_of_two(num)
    three_data = Sum_of_three(num)
    four_data = Sum_of_four(num)
    five_data = Sum_of_five(num)
    print("{} can be expressed as a sum of two squares:{} \n a sum of three squares:{} \n a sum of four squares:{} \n a sum of five squares:{}".format(num,two_data,three_data,four_data,five_data))

    

    

