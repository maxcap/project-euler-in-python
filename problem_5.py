'''
Project Euler Problem 5 in Python
https://projecteuler.net/problem=5

SMALLEST MULTIPLE

"2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder."

Problem:
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

def check(n):
	for i in range(11, 21):
		if n % i != 0:
			return False
	return True

if __name__ == '__main__':
	n = 2520
	while not check(n):
		n += 2520   # 2520 must be a factor to satisfy 1-10 no remainder.
	print n