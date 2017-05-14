# Calculates square root using B-search.


# This controls the degree of accuracy of results.
# A higher number gives a higher accuracy. +-
# However, 18 is the limit my laptop can handle without freezing.
ACCURACY = 18


def sqrt(n):
	assert n > 0

	_min = 0
	_max = n - 1
	counter = 0
	guess = (_min + _max) / 2.0

	while(counter != ACCURACY):
		guess = (_min + _max) / 2.0
		if(guess**2 > n):
			_max = guess
		elif(guess**2 < n):
			_min = guess
			counter += 1

	return (_min + _max) / 2.0



#sqrt(100)             ---> 9.99999999987
#sqrt(10)              ---> 3.16227766017
#sqrt(121)             ---> 10.9999997914
#sqrt(400)             ---> 20.0
#sqrt(472732987487479) ---> 21742423.6773
