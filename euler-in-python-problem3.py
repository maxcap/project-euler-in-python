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

# From Project Euler PDF: After first improvement
def all_prime_factors(n):
	# 2 is the only even prime, so by treating it separately we can increase
	# factor with 2 every step.
	while n % 2 == 0:
		n /= 2
	# Start while loop with factor 3
	factor = 3
	while n > 1 and factor ** 2 <= n:
		while n % factor == 0:
			n /= factor
			yield factor
		factor += 2  # loop over odd only. We dealt with all evens earlier.
	yield n

if __name__ == '__main__':
	N = 600851475143
	print max(all_prime_factors(N))