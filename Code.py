########################### Navie/ Iterative Part ############################################

# Python3 program to print all
# subset combination of n
# element in given set of r element .

# arr[] ---> Input Array
# data[] ---> Temporary array to
#             store current combination
# start & end ---> Starting and Ending
#                 indexes in arr[]
# index ---> Current index in data[]
# r ---> Size of a combination
#     to be printed


def combinationsSets(arr, n, r,
                    index, data, i,allsubsets):
    # Current combination is
    # ready to be printed,
    # print it
    
    
    if(index == r):
        temp=[0]*r
        for j in range(r):
           temp[j]=data[j]
        allsubsets.append(temp)
        return
    


    # When no more elements
    # are there to put in data[]
    if(i >= n):
        return

    # current is included,
    # put next at next
    # location
    data[index] = arr[i]
    combinationsSets(arr, n, r, index + 1, data, i + 1,allsubsets)
    
    # current is excluded,
    # replace it with
    # next (Note that i+1
    # is passed, but index
    # is not changed)
    combinationsSets(arr, n, r, index, data, i + 1,allsubsets)


# The main function that
# prints all combinations
# of size r in arr[] of
# size n. This function
# mainly uses combinationsSets()
def getAllcombinations(arr, n, r,allsubsets):

    # A temporary array to
    # store all combination
    # one by one
    data = list(range(r))
    
    # Print all combination
    # using temporary
    # array 'data[]'
    combinationsSets(arr, n, r,
                    0, data, 0,allsubsets)

def getOtherSubset(original_arr,remove_list):
    
    test_list = original_arr.copy()
    # using remove() to perform task
    # handled exceptions.
    for i in remove_list:
        try:
            test_list.remove(i)
        except ValueError:
            pass
    return test_list



def findMin(arr, n):
    # Compute total sum
    # of elements
    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]
    
    #print(sumTotal)
    if int((sumTotal) % 2) != 0:
        return 1
    else:
        return 0 

def findSubsetwithMinDiff(allsubsets, original_arr, minDiff):
    
    n = int(len(allsubsets))
    finallsubsets = [[]*1]*1
    for i in range(n):
        user1_values = allsubsets[i] 
        user2_values = getOtherSubset(original_arr,allsubsets[i])
        diff = abs(sum(user1_values)-sum(user2_values))
        #print("diff" + str(diff))
        if (diff==minDiff) :
            #print("User1 Coins " + str(allsubsets[i]))
            #print("User2 Coins " + str(getOtherSubset(original_arr,allsubsets[i])))
            if  not in_list(user1_values, finallsubsets) :            
               finallsubsets.append(user1_values)
               finallsubsets.append(user2_values)
          
            

        
       
    return finallsubsets #set(tuple(element) for element in finallsubsets)

def in_list(user1_values, finallsubsets):
    for i, sublist in enumerate(finallsubsets):
        #print(sublist)
        str_value = ",".join(str(user1_values))
        str_list =  ",".join(str(sublist))
        if str_value ==  str_list:
           return True
        
    return False

####################################Dynamic Programming Part###################################
# Python3 program to partition an array of
# non-negative integers into two subsets
# such that average of both the subsets are equal
dp = []
res = []
original = []
total_size = int(0)

# Function that returns true if it is possible
# to use elements with index = ind to construct
# a set of s ize = curr_size whose sum is curr_sum.
def possible(index, curr_sum, curr_size):
    
    index = int(index)
    curr_sum = int(curr_sum)
    curr_size = int(curr_size)
    
    global dp, res
    
    # Base cases
    if curr_size == 0:
        return (curr_sum == 0)
    if index >= total_size:
        return False
    
    # Which means curr_sum cant be
    # found for curr_size
    if dp[index][curr_sum][curr_size] == False:
        return False
    
    if curr_sum >= original[index]:
        res.append(original[index])
        
        # Checks if taking this element
        # at index i leads to a solution
        if possible(index + 1,
                    curr_sum - original[index],
                    curr_size - 1):
            return True
            
        res.pop()
    
    # Checks if not taking this element at
    # index i leads to a solution
    if possible(index + 1, curr_sum, curr_size):
        return True
    
    # If no solution has been found
    dp[index][curr_sum][curr_size] = False
    return False

# Function to find two partitions
# having minimum difference
def dynamicPartition(Vec):
    
    global dp, original, res, total_size
    
    # Sort the vector
    Vec.sort()
    
    if len(original) > 0:
        original.clear()
    
    original = Vec
    
    if len(dp) > 0:
        dp.clear()
    if len(res) > 0:
        res.clear()

    total_sum = 0
    total_size = len(Vec)

    for i in range(total_size):
        total_sum += Vec[i]
    #print(total_sum)
    # Building the memoization table
    dp = [[[True for _ in range(total_size)]
                for _ in range(total_sum + 1)]
                for _ in range(len(original))]
    
    for i in range(1, total_size):
        
        # Sum_of_Set1 has to be an integer
        if int((total_sum * i) % 2) != 0:
            Sum_of_Set1 = int(total_sum/2)+1
        else:
            Sum_of_Set1 = int(total_sum/2) 
        
            
        #Sum_of_Set1 = int(total_sum/2) #* i) / total_size
        #print(Sum_of_Set1)
        # We build our solution vector if its possible
        # to find subsets that match our criteria
        # using a recursive function
        if possible(0, Sum_of_Set1, i):

            # Find out the elements in Vec,
            # not in res and return the result.
            ptr1 = 0
            ptr2 = 0
            res1 = res
            res2 = []
            
            while ptr1 < len(Vec) or ptr2 < len(res):
                if (ptr2 < len(res) and
                    res[ptr2] == Vec[ptr1]):
                    ptr1 += 1
                    ptr2 += 1
                    continue
                    
                res2.append(Vec[ptr1])
                ptr1 += 1

            ans = []
            ans.append(res1)
            ans.append(res2)
            
            #print(ans)
                
            return ans
    
    # If we havent found any such subset.
    ans = []
    return ans


################################ Driver Code ############################################
inputFileHandle = open('inputPS08.txt', "r")  # Create Input File Handle to Read Contents.
inputFileLines = inputFileHandle.readlines()  # Reading All Lines from Input File.

outputFileHandle = open('outputPS08.txt', "w")
test_case_no = 0

for inputFileLine in inputFileLines:
    arr_list = inputFileLine.translate({ord(i): None for i in '[]\n'}).split(',')
    arr = [eval(i) for i in arr_list]
    
    test_case_no=test_case_no+1
    print(str(test_case_no))
    

   
    original_arr = arr.copy()
    dp_arr = arr.copy()
    no_of_users =2
    n = len(arr)
   
    #r = int(len(arr)/no_of_users)
    allsubsets = [[0]]
    minDiff = findMin(arr,n)
    #print(minDiff)
    #print("Min diff for after creating 2 sets is :" + str(minDiff))
    ##generate all combinations for subsets from given set
    for k in range(n):
        getAllcombinations(arr, n, k,allsubsets)


    print("############# Ierrative Program Call ##########################")
    ##Iterate Through all the sets to find set matching minimum difference
    IterSol = findSubsetwithMinDiff(allsubsets, original_arr, minDiff)
    
    
    outputFileHandle.write('\n' + "Naive method: " + '\n' )
    outputFileHandle.write("Test Case: " + str(test_case_no) + '\n' )
    if len(IterSol) > 1:
        for i in range(1,len(IterSol)-1):
            print("User1 Coins " + str(IterSol[i]) + " SumTotal = " + str(sum(IterSol[i])))
            
            outputFileHandle.write("First Child " + str(IterSol[i]) + '\n')  
            i+=1
            print("User2 Coins " + str(IterSol[i]) + " SumTotal = " + str(sum(IterSol[i])))
            #print(" ")
            outputFileHandle.write("Second Child " + str(IterSol[i]) + '\n')  
            outputFileHandle.flush()
            break
    else:
        print("Unable to split the given list " + str(arr)) 
        outputFileHandle.write("Unable to split the given list " + str(arr) + '\n')
        outputFileHandle.flush()
       
    
    print("############# Dynamic Program Call ##########################")

    outputFileHandle.write('\n' + "Dynamic programming: " + '\n' )
    outputFileHandle.write("Test Case: " + str(test_case_no) + '\n' )
    finalSol = dynamicPartition(dp_arr)
    #print(finalSol)
    if len(finalSol) > 1:
        for i in range(0,len(finalSol)-1):
            print("User1 Coins " + str(finalSol[i]) + " SumTotal = " + str(sum(finalSol[i])))
            outputFileHandle.write("First Child " + str(finalSol[i]) + '\n')  
           # print("User2 Coins " + str(getOtherSubset(original_arr,allsubsets[i])))
            i+=1
            print("User2 Coins " + str(finalSol[i]) + " SumTotal = " + str(sum(finalSol[i])))
            outputFileHandle.write("Second Child " + str(finalSol[i]) + '\n') 
            outputFileHandle.flush()
            print(" ")
    else:
        print("Unable to split the given list " + str(arr))
        outputFileHandle.write("Unable to split the given list " + str(arr) + '\n')
        outputFileHandle.flush()
    
        
        
        
    #outputFileHandle.close()
    

    
