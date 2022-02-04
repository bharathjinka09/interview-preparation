# nums = [1,2,2,2,3,3,4,5,5,5,7]

# unique_elemts = []

# def get_unique_elements(nums):
# 	for i in nums:
# 		if i not in unique_elemts:
# 			unique_elemts.append(i)
# 	return unique_elemts

# output = get_unique_elements(nums)

# print(output)


def sum_two_numbers(nums, target):
	dictionary = {}
	array = []

	for i in range(len(nums)):
		secondNo = target-nums[i]
		# print(secondNo,"secondNo")

		if(secondNo in dictionary.keys()):
			# secondIndex = nums.index(secondNo)
			secondIndex = dictionary[secondNo]


			# print(secondIndex,"secondIndex")

			if(i != secondIndex):
				# print(i,"i")
				return sorted([i,secondIndex])
		else:
			dictionary[nums[i]] = i

result = sum_two_numbers([1,2,3],3)
# print(result)


# def test_upload(client):
#     data = {
#         'Data': [20.0, 30.0, 401.0, 50.0],
#         'Date': ['2017-08-11', '2017-08-12', '2017-08-13', '2017-08-14'],
#         'Day': 4
#     }
#     url = '/upload/'

#     response = client.post(url, json=data)

#     assert response.content_type == 'application/json'
#     assert response.json['Result'] == 39


# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper
# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper

def reverse_string_decorator(function):
	def wrapper():
		func = function()
		reverse_string = func[::-1]
		return reverse_string
	return wrapper

@splitter_decorator # this is executed next
@lowercase_decorator # this is executed second
@reverse_string_decorator # this is executed first
def hello():
   return 'Hello World'
print(hello()) 



















