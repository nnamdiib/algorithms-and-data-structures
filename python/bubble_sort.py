# !/usr/bin/env python 

# My implementation of bubble sort

# This one sorts from smallest to biggest. 
#  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
f = [8,5,3,1,9,6,0,7,4,2,5]		

def bubble(ar):
	# Make a copy
	arr = ar[:]
	
	# Loop through array, compare each item to successive item. 
	# Something feels weird about nested loops. But it works so whatever. 
	for i in range(len(arr)):	
		for i in range(len(arr)):
			# We will get a list index error if we loop till the last item. 
			if i != len(arr) - 1:	

				# Change the sign to '<' to sort in descending order.
				if arr[i] > arr[i + 1]:
					print "Sorting..."				
					arr[i], arr[i + 1] = arr[i + 1], arr[i]
	print "All done!"		
	return arr	

def main():
	test = bubble(f)
	print test

if __name__ == "__main__":
	main()


		

