from Assignment3  import*

nums = input("Enter the numbers you would like to add and multiply together, separated by commas. \n")
numlist = list(map(int,nums.split(',')))
print('sum: ', sum_all(numlist),'\n','product: ', multiply_all(numlist),'\n',sep='')