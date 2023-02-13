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

def main():
    nums = input("Enter the numbers you would like to add and multiply together, separated by commas. \n")
    numlist = list(map(int,nums.split(',')))
    print('sum: ', sum_all(numlist),'\n','product: ', multiply_all(numlist),'\n',sep='')
    
    


main()