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

    for i in range(int(num) - 1):
        if Is_Square(num - 1 - i):
            return num - 1 - i
    return 0


def Sum_of_n(num,n):
    #returns a list of length n+1 containing bool and summands

    #if n == 1 the problem reduces to if n is a square
    if n == 1:
            return [Is_Square(num),math.sqrt(num)]
    
    start = num
    while start > num/n:  #stops calculation if point is reached where n*[value to check] = num || before: start != 0

        #find the next smaller square number of start
        a = next_smaller_square(start)

        #if next smaller square of a is 0, then a is 1, therefore the loop ends
        if a == 0:  
            return [False] + n * ["x"]
        
        #calculate the remaining sum to check
        b = num - a 
        
        #if n=2 and we found one next smaller square of n, the problem reduces to if n-a is asquare number
        if n == 2:
            is_sum_n_minus_1 = [Is_Square(b),math.sqrt(b)]
        #The problem reduces to "Is the remaining number b a sum of n-1 squares"
        elif n > 2:
            is_sum_n_minus_1 = Sum_of_n(b,n - 1)
        else: #this case should never be accessed
            print("how tf did you get here")
            return [False] + n * ["y"]

        #checking if is-b-a-sum-of-squares was successful
        if is_sum_n_minus_1[0]:
            #a is a square so it has a root
            roota = math.sqrt(a)
            #extract the roots out of the output of the check if b is a sum of squares
            stuff = [is_sum_n_minus_1[i] for i in range(1, n)]

            #puzzling together the output, this is the end of a successful check if num is a sum of n squares
            return [True,roota] + stuff 
        else:
            #the b is not a sum of n-1 squares, so we go to the second next smaller square of num and check if the 
            #difference is a sum of n-1. Then we check the third next smaller square, then the fourth, ...
            #until the next-smaller-square (=nss) times n is smaller than num. In this case there has to be a bigger square than 
            #the nss to fill the difference between num and the nss. This bigger square must have been checked before.
            # --> The loop ends
            start = a

    #This is hit if the Check for a next smaller square is unsuccessful
    return [False] + n * ["z"]


#finding degeneracy
def degeneracy(num,n):
    #returns array containing sum_of_n and degeneracy

    if n == 1:
        #xxxxxxxxx
        return [Is_Square(num),1,[math.sqrt(num)]]

    sum1 = Sum_of_n(num,n)
    
    if sum1[0]:
        #start calculating degeneracy of first solution of sum_of_n
        start = sum1[1]

        #counter of degeneracy
        deg_num_n = 0

        #return array
        arr = []

        while start**2 >= 1 : #For degeneracy where the order of the summands matters, set num/n -> 1

            #calculate difference of num and start^2
            b = num - (start **2)

            #calculate degeneracy of (b = sum of n-1 squares)
            deg_2nd_degree = degeneracy(b,n-1)

            if(deg_2nd_degree[0]): #if there is at least one solution
                #the degeneracy increases by the degeneracy of (b = n-1 squares)
                deg_num_n += deg_2nd_degree[1]

                #extract solutions from deg_2nd_degree
                for i in range(2,deg_2nd_degree[1] + 2):
                    arr += [[start] + [deg_2nd_degree[i][j] for j in range(n-1)]]

            start = start - 1


        return [sum1[0],deg_num_n] + arr
    else:
        deg_num_n = 0
        return [sum1[0],deg_num_n] + [n*['z']]
    


if __name__ == '__main__':
    n = 3
    for num in range(1,100):
        deg = degeneracy(num,n)
        sumo = Sum_of_n(num,n)

        print(num,' degen: ', deg)
        #print('Sum of n ', sumo)

        if deg[0] != sumo[0]: #comparing bool values of sum of n and degeneracy
            raise(ValueError)
        if deg[deg[1]+1] == 3: #checking for Indexerrors/ errors in length of returned array
            raise(IndexError)
        
        if deg[0]: #comparing all degenerated results if they are the same
            check_1 = 0
            for i in range(n):
                check_1 += (deg[2][i])**2
            
            if check_1 != num: 
                raise(ValueError)

            for j in range(2,deg[1]-1):
                check_2 = 0
                for i in range(n):
                    check_2 += (deg[j][i])**2

                if check_2 != check_1: 
                    raise(ValueError)

    '''
    inp = 1
    inp = input("A positive Integer:")
    inp2 = input("A number of summands:")

    intinp = int(inp)
    intinp2 = int(inp2)
    
    print("{} can be expressed as a sum of {} squares: {}".format(inp,inp2,Sum_of_n(intinp,intinp2)))

    print("------------------------------------------------")
    
    #setting limits for range ouput
    num_lower = 4000
    num_upper = 4100

    sum_lower = 3
    sum_upper = 3

    trueorfalse = False #print Values for true or false

    print("Checking values between {} and {} if they can be expressed as a sum of {} to {} of squares.".format(num_lower,num_upper,sum_lower,sum_upper))
    print("Printing output, where results are {}".format(trueorfalse))
    for i in range(num_lower,num_upper + 1):
        for j in range(sum_lower,sum_upper + 1):
            result = Sum_of_n(i,j)
            if result[0] == trueorfalse:
                print("{} can be expressed as a sum of {} squares: {}".format(i,j, result)) 
    '''
