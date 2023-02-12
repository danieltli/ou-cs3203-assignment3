def sum_all(numList):
    ans = 0;
    if(type(numList) != list):
        print("Not a List")
    for x in numList:
        ans += x
    return ans


