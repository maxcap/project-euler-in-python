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

# From Project Euler PDF: Crude Version (with a Pythonic twist)
def all_prime_factors(n):
	yield 1
	factor = 2
	while n > 1:
		while n % factor == 0:
			yield factor
			n /= factor
		factor += 1

if __name__ == '__main__':
	N = 600851475143
	print max(all_prime_factors(N))