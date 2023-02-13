from Assignment3  import*

nums = input("Enter the numbers you would like to reverse, add and multiply together, separated by commas. \n")
numlist = list(map(int,nums.split(',')))
print('reversed: ',reverse(numlist),'\n','sum: ', sum_all(numlist),'\n','product: ', multiply_all(numlist),'\n',sep='')