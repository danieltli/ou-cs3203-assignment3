def sum_all(numList):
    #sum all ints in a list
    ans = 0;
    if(type(numList) != list):
        print("Not a List")
    for x in numList:
        ans += x
    return ans

def multiply_all (numList):
    #multiplies all numbers in a list
    ans = 0;
    if(type(numList) != list):
        print("Not a List")
    for idx, x in enumerate(numList):
        if (numList[idx] != 0 and  ans == 0):
         ans = x
        else:
            ans *= x
            
    return ans

def reverse(numList):
    #reverse all elements in a list
    return list(reversed(numList))

def doNothing():
    


