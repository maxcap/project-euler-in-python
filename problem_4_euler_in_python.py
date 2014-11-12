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
	largest_palindrome = 0
	for i in range(999, 99, -1):
		for j in range(i, 99, -1):
			if i * j <= largest_palindrome:
				break
			if is_palindrome(i * j) and i * j > largest_palindrome:
				largest_palindrome = i * j
	return largest_palindrome

# This script takes ~0.015 secs to complete.
if __name__ == '__main__':
	print find_palindromes()
