'''
Project Euler Problem 4 in Python
https://projecteuler.net/problem=4

LARGEST PALINDROME PRODUCT

"A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.""

Problem:
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def base_ten_blocks(x):
	'''
	Splits apart an integer into its constituent counting blocks.

	e.g. input:		1234
		 output:	[1000, 200, 30, 4]
	'''
	y, z = 0, 0
	blocks = []
    # e.g. for 1234
    # 1st loop:  % 10    --> 4    --> 4
    # 2nd loop:  % 100   --> 34   --> 30
    # 3rd loop:  % 1000  --> 234  --> 200
    # 4th loop:  % 10000 --> 1234 --> 1000
	while x != y:
	    y = x % (10 ** (z + 1))
	    blocks.append(y / (10 ** z) * (10 ** z))
	    z += 1
	return blocks

def num_backwards(base_blocks):
	'''Takes base 10 blocks of the original number, flips them into the reverse
	base blacks, then returns the sum of these new base blocks to give the
	original number but back-to-front.'''
	new_blocks = []
	a = len(base_blocks) - 1
    # e.g. for 1234
    # 1st loop:  4    --> x 10^3  --> 4000
    # 2nd loop:  30   --> x 10^1  --> 300
    # 3rd loop:  200  --> x 10^-1 --> 20
    # 4th loop:  1000 --> x 10^-3 --> 1
	for block in base_blocks:
	    new_blocks.append(block * (10 ** a))
	    a -= 2 
	return int(sum(new_blocks))

def find_palindromes():
	'''Returns a list of all palindromes found for the product of two 3-digit
	numbers.'''
	for i in range(100, 1000):
		for j in range(100, 1000):
			product = i * j
			product_backwards = num_backwards(base_ten_blocks(product))
			if product == product_backwards:
				yield product

# This script takes ~9 secs to complete.
# The challenge is... if you start from 999 down and break when you find the
# first value, how do you know that this is the max product?
if __name__ == '__main__':
	print max(find_palindromes())
