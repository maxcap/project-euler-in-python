'''
Project Euler Problem 4 in Python
https://projecteuler.net/problem=4

LARGEST PALINDROME PRODUCT

"A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.""

Problem:
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
	'''Returns True if number is a palindrome'''
	return n == int(str(n)[::-1])

def find_palindromes():
	'''Returns a list of all palindromes found for the product of two 3-digit
	numbers.'''
	for i in range(100, 1000):
		for j in range(100, 1000):
			product = i * j
			if is_palindrome(product):
				yield product

# This script takes ~1.5 secs to complete.
# The challenge is... if you start from 999 down and break when you find the
# first value, how do you know that this is the max product?
if __name__ == '__main__':
	print max(find_palindromes())
