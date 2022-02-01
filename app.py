# def fib(num):
# 	a,b = 0,1
# 	for i in range(0,num):
# 		 yield "{}:{}".format(i+1,a)
# 		 a,b=b,a+b

 
# for item in fib(10):
# 	print(item)
















# def fib(num):
# 	a,b=0,1
# 	for i in range(0,num):
# 		yield "{}:{}".format(i+1,a)
# 		a,b=b,a+b
		
# for j in fib(10):
# 	print(j)



# test_list = [1,3,4,5,3,4]
# print ("The original list is : " +  str(test_list))

# unique_list = []

# for i in test_list:
# 	if i not in unique_list:
# 		unique_list.append(i)

# print((unique_list))



def twoSum(nums, target):
        dictionary = {}
        answer = []
        
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})

res = twoSum([1,2,3],3)
print(res)





























