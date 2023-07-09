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

    for i in range(num - 1):
        if Is_Square(num - 1 - i):
            return num - 1 - i
    return 0

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
    if n ==1:
            return [Is_Square(num),math.sqrt(num)]
    
    start = num
    while start != 0:
        a = next_smaller_square(start)
        if a == 0:  #if next smaller square of a is 0, then a is 1, therefore the loop ends
            return [False] + n * ["x"]
        
        b = num - a 
            
        if n == 2:
            is_sum_n_minus_1 = [Is_Square(b),math.sqrt(b)]
        elif n > 2:
            is_sum_n_minus_1 = Sum_of_n(b,n - 1)
        else:
            print("how tf did you get here")
            return [False] + n * ["y"]

        if is_sum_n_minus_1[0]:
            roota = math.sqrt(a)
            stuff = [is_sum_n_minus_1[i] for i in range(1, n)]
            return [True,roota] + stuff
        else:
            start = a

    return [False] + n * ["z"]

if __name__ == '__main__':
    inp = 1
    inp = input("A positive Integer:")
    inp2 = input("A number of summands:")

    intinp = int(inp)
    intinp2 = int(inp2)
    
    print("{} can be expressed as a sum of {} squares: {}".format(inp,inp2,Sum_of_n(intinp,intinp2)))

    print("------------------------------------------------")
    
    #setting limits for range ouput
    num_lower = 4000
    num_upper = 5000

    sum_lower = 2
    sum_upper = 3 

    trueorfalse = False #print Values for true or false

    print("Checking values between {} and {} if they can be expressed as a sum {} to {} of squares.".format(num_lower,num_upper,sum_lower,sum_upper))
    print("Printing output, where results are {}".format(trueorfalse))
    for i in range(num_lower,num_upper + 1):
        for j in range(sum_lower,sum_upper + 1):
            result = Sum_of_n(i,j)
            if result[0] == trueorfalse:
                print("{} can be expressed as a sum of {} squares: {}".format(i,j, result))