# !/usr/bin/env python 

# My implementation of bubble sort

'''
Analysis
Order of Growth: O(N^2)
'''

#  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,8,9] ; if ascending order flag 'asc' set to True
num_list = [8,5,3,1,9,6,0,7,4,2,5]

def bubble(_list, asc=True):
	# Make a copy
	arr = _list[:]
	
	# Loop through array, compare each item to successive item. 
	# Something feels weird about nested loops. But it works so whatever. 
	# print "Sorting..."
	for i in range(len(arr)):	
		for i in range(len(arr)):
			# We will get a list index error if we loop till the last item. 
			if (i != len(arr) - 1):
				# change sorting order based on asc default argument flag
				# By default asc is set True and the function sorts in ascending order
				# When asc is set to False, it sorts in descending order
				compare = lambda a,b : a > b if asc else a < b
				if compare(arr[i], arr[i + 1]):									
					arr[i], arr[i + 1] = arr[i + 1], arr[i]
	# unnecessary side effect				
	# print "All done!"		
	return arr

# tests	for both ascending and descending orders
def test():
	assert bubble(num_list) == sorted(num_list)
	assert bubble(num_list, asc=False) == sorted(num_list, reverse=True)

def main():
	test()
	
	print bubble(num_list)
	print bubble(num_list, asc=False)

if __name__ == "__main__":
	main()
