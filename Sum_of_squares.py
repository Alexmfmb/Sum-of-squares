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


def Sum_of_n(s:int,n:int):
    #returns a list of length n+1 containing bool and summands

    #if n == 1 the problem reduces to if n is a square
    if n == 1:
            return [Is_Square(s),math.sqrt(s)]
    
    #first start value is the value of the sum
    start = s

    while start * n > s:  #stops calculation if point is reached where n*[value to check] = s || before: start != 0

        #find the next smaller square number of start
        a = next_smaller_square(start)

        #if next smaller square of a is 0, then a is 1, therefore the loop ends
        if a == 0:  
            return [False] + n * ["x"]
        
        #calculate the remaining sum to check
        b = s - a 
        
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
def degeneracy(s:int,n:int):
    #returns array containing sum_of_n and degeneracy

    if n == 1:
        sq = Is_Square(s)
        if(sq):
            return [Is_Square(s),1,[math.sqrt(s)]]
        else:
            return [False,0,['z']]
        

    sum1 = Sum_of_n(s,n)
    
    if sum1[0]: #if there is at least one solution:

        #counter of degeneracy
        deg_s_n = 0

        #return array
        arr = []
        
        start = sum1[1] #start with first square of the solution of (s,n)

        while start**2 * n >= s : #For degeneracy where the order of the summands matters, set s -> n

            #calculate difference of s and start^2
            b = s - (start **2)

            #calculate degeneracy of (b = sum of n-1 squares) := (b, n-1)
            deg_2nd_degree = degeneracy(b,n-1)

            if(deg_2nd_degree[0]): 
                #if there is at least one solution for second degree degeneracy
                
                if((max(deg_2nd_degree[2]) <= start)):
                    #(max(deg_2nd_degree[2]) <= start)
                    '''if the maximum number of the second degree degeneracy is larger than the start number, 
                    this solution must have been checked before, because this algorithm checks solution with decreasing 
                    value of the first number of the solution.
                    for (233,3):
                    [15,2,2] then [14,6,1] then [12,8,5] 
                    so if we check [8,...] and find the solution [8,12,5] the max of this solution is larger than the start value which is ?
                    '''

                    #the degeneracy increases by the degeneracy of (b, n-1)
                    deg_s_n += deg_2nd_degree[1]

                    #extract solutions from deg_2nd_degree
                    for i in range(2,deg_2nd_degree[1] + 2):
                        arr += [[start] + [deg_2nd_degree[i][j] for j in range(n-1)]]

            start = start - 1


        return [sum1[0],deg_s_n] + arr
    else:
        deg_s_n = 0
        return [sum1[0],deg_s_n] + [n*['z']]



#finding degeneracy
def degeneracy_long(s:int,n:int):
    #returns array containing sum_of_n and degeneracy

    if n == 1:
        sq = Is_Square(s)
        if(sq):
            return [Is_Square(s),1,[math.sqrt(s)]]
        else:
            return [False,0,['z']]
        

    sum1 = Sum_of_n(s,n)
    
    if sum1[0]: #if there is at least one solution:

        #counter of degeneracy
        deg_s_n = 0

        #return array
        arr = []
        
        start = sum1[1] #start with first square of the solution of (s,n)

        while start**2 >= 1 : #this makes the code check ALL permutations. Compare other degeneracs function

            #calculate difference of s and start^2
            b = s - (start **2)

            #calculate degeneracy of (b = sum of n-1 squares) := (b, n-1)
            deg_2nd_degree = degeneracy_long(b,n-1)

            if(deg_2nd_degree[0]): 
                #if there is at least one solution for second degree degeneracy

                #the degeneracy increases by the degeneracy of (b, n-1)
                deg_s_n += deg_2nd_degree[1]

                #extract solutions from deg_2nd_degree
                for i in range(2,deg_2nd_degree[1] + 2):
                    arr += [[start] + [deg_2nd_degree[i][j] for j in range(n-1)]]

            start = start - 1


        return [sum1[0],deg_s_n] + arr
    else:
        deg_s_n = 0
        return [sum1[0],deg_s_n] + [n*['z']]




if __name__ == '__main__':

    n = 3
    s_min = 100
    s_max = 200
    for s in range(s_min,s_max):
        deg = degeneracy(s,n)
        deg_l = degeneracy_long(s,n)
        sumo = Sum_of_n(s,n)

        print(s,' degen_norm:\t', deg)
        print(s,' degen_long:\t', deg_l)
        #print('Sum of n ', sumo)

        if deg[0] != sumo[0]: #comparing bool values of sum of n and degeneracy
            raise(ValueError)
        if deg[deg[1]+1] == 3: #checking for Indexerrors/ errors in length of returned array
            raise(IndexError)
        
        if deg[0]: #comparing all degenerated results if they are the same
            check_1 = 0
            for i in range(n):
                check_1 += (deg[2][i])**2
            
            if check_1 != s: 
                raise(ValueError)

            for j in range(2,deg[1]-1):
                check_2 = 0
                for i in range(n):
                    check_2 += (deg[j][i])**2

                if check_2 != check_1: 
                    raise(ValueError)