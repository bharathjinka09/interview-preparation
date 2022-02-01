# def fib(num):
# 	a,b = 0,1
# 	for i in range(0,num):
# 		 yield "{}:{}".format(i+1,a)
# 		 a,b=b,a+b

 
# for item in fib(10):
# 	print(item)















# fibonacci numbers
# def fib(num):
# 	a,b=0,1
# 	for i in range(0,num):
# 		# yield "{}:{}".format(i+1,a)
# 		yield a
# 		a,b=b,a+b
		
# for j in fib(10):
# 	print(j)


# Linear Search

# data = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]

# for i in range(len(data)): 
#     if data[i] == 7:
#         print(i)


# Binary Search

def binary_search(arr, elem):

    low = 0
    high = len(arr) - 1

    while low <= high:
      
        middle = (low + high)//2
       
        if arr[middle] == elem:
            return middle
        elif arr[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1
    
arr = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]
elem = 7

output = binary_search(arr, elem)
print(output)

# test_list = [1,3,4,5,3,4]
# print ("The original list is : " +  str(test_list))

# unique_list = []

# for i in test_list:
# 	if i not in unique_list:
# 		unique_list.append(i)

# print((unique_list))



# def twoSum(nums, target):
#         dictionary = {}
#         answer = []
        
#         for i in range(len(nums)):
#             secondNumber = target-nums[i]
#             if(secondNumber in dictionary.keys()):
#                 secondIndex = nums.index(secondNumber)
#                 if(i != secondIndex):
#                     return sorted([i, secondIndex])
                
#             dictionary.update({nums[i]: i})

# res = twoSum([1,2,3],3)
# print(res)





























