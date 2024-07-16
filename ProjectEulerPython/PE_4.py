# Written 02/23/2021 by Christina Mazilu
# Project Euler Question 4: https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99
# Find the largest palindrome made from the product of two 3 digit numbers.


def largestPalin(n):
    allPalin = []
    lower = 10**(n-1)
    upper = 10**n
    for i in range(lower, upper):
        for j in range(lower, upper):
            product = j*i
            if checkPalin(product):
                allPalin.append(product)
    return max(allPalin)

def checkPalin(number):
    n = str(number)
    isPalindrome = True
    for i in range(0, len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            isPalindrome = False
    return isPalindrome


print(largestPalin(2))
