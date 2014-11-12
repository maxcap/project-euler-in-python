'''
Project Euler Problem 3 in Python
https://projecteuler.net/problem=3

LARGEST PRIME FACTOR

"The prime factors of 13195 are 5, 7, 13 and 29.""

Original Problem:
What is the largest prime factor of the number 600851475143?

Modified Problem: *
What is the largest prime factor of the number N?
'''

# Note - Python iterables are limited to 536,870,912 elements. Therefore, avoid
# 		 any attempt to make an iterable of all values up to N. It will crash.

# This function is hard to explain without walking through it on a whiteboard.
def largest_prime_factor(n):
	'''Return the largest prime factor for integer n.'''
	# Start at 2. Division by 1 is redundant.
	i = 2
	# Why stop at the square of i? It is equivalent to 'while i < n * 0.5'.
	# e.g. for a * b = 100, it is impossible for both a and b to be above 10 and
	# also satisfy a * b = 100.
	while i * i < n:     # important - Python re-evaluates condition on each pass.
		while n % i == 0:
			n /= i
		i += 1
	return n
	
if __name__ == '__main__':
	N = 600851475143
	print largest_prime_factor(N)