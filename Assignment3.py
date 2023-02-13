def sum_all(numList):
    ans = 0;
    if(type(numList) != list):
        print("Not a List")
    for x in numList:
        ans += x
    return ans

def multiply_all (numList):
    ans = 0;
    if(type(numList) != list):
        print("Not a List")
    for idx, x in enumerate(numList):
        if (numList[idx] != 0 and  ans == 0):
         ans = x
        else:
            ans *= x
            
    return ans
    
    


