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
# print(output)

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
#             print(secondNumber,"secondNumber")
#             if(secondNumber in dictionary.keys()):
#                 secondIndex = nums.index(secondNumber)
#             	print(secondIndex,"secondIndex")
#             	# print(dictionary,"dictionary")

#                 if(i != secondIndex):
#                     return sorted([i, secondIndex])
                
#             dictionary.update({nums[i]: i})
# res = twoSum([1,2,3],3)
# print(res)




# def bi_search(arr,elem):
# 	low = 0
# 	high = len(arr)-1

# 	while low <= high:
# 		middle = (low+high)//2

# 		if arr[middle] == elem:
# 			return middle
# 		elif arr[middle] > elem:
# 			high = middle - 1
# 		else:
# 			low = middle + 1

# 	return -1

# print(bi_search([1,2,3,4,4,6,7,9],7))


# class and static methods
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_birth_year(cls,name,year):
        return cls(name,date.today().year-year)

    # for utility or helper functions, cannot instantiate object
    @staticmethod
    def isAdult(age):
        return age > 18

p1=Person("bhaarth",26)

p2 = Person.from_birth_year("ram",1995)

p3 = Person.isAdult(55)

print(p1.age)

print(p2.age)

print(p3)

print(Person.isAdult(22))




# shallow copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list,id(old_list))
print("New list:", new_list,id(new_list))

'''
o/p:-
----
Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

'''

# deep copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list,id(old_list))
print("New list:", new_list,id(new_list))

# o/p
''' 
Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
'''














