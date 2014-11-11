'''Project Euler Problem 1 in Python (https://projecteuler.net/problem=1)

"If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23."

Original Problem:
Find the sum of all the multiples of 3 or 5 below 1000.

Modified Problem:
Find the sum of all the multiples of x or y below N.

This module tackles the modified problem.
'''

def arithmetic_series(N, d):
	'''Returns the sum of an arithmetic sequence, the sequence being multiples
	of d below N.'''
	# n is the number of terms.
	# Problem states 'below N', hence (N - 1)
	# Makes use of Python 2.7 floor division of ints.
	n = (N - 1) / d 
	
	# Arithmetic series formula:
		# Sn = n / 2 * (2 * a1 + (n - 1) * d)
	# Where:
		# Sn 	sum of the total number of the series
		# a1	first number of the series
		# n 	number of terms
		# d 	difference between two successive numbers

	# In this problem, a1 is always equal to d.
	return n * (2 * d + (n - 1) * d) / 2 

def main():
	'''Main entry point for script.'''
	print (arithmetic_series(N, x)
		 + arithmetic_series(N, y)
		 - arithmetic_series(N, x * y)) # because counted twice


if __name__ == '__main__':
	N = 1000
	x = 3
	y = 5
	main()