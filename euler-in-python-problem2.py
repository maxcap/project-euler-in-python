'''Project Euler Problem 2 in Python (https://projecteuler.net/problem=2)

"Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..."

Original Problem:
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

Modified Problem:
By considering the terms in the Fibonacci sequence whose values do not exceed
N, find the sum of the even-valued terms.

This module tackles the modified problem.
'''

def even_fib_terms(N):
	'''Returns the sum of the even-valued terms in a Fibonacci sequence whose
	values do not exceed N.'''
	a, b = 0, 1
	while a <= N:
		if not a % 2:
			yield a
		a, b = b, a + b

def main():
	'''Main entry point for script.'''
	print sum(even_fib_terms(N))

if __name__ == '__main__':
	N = 4000000
	main()