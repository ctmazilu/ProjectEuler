# Written 02/24/2021 by Christina Mazilu
# Project Euler Question 6: https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import numpy as np
from pytictoc import TicToc

allSumSquares = []
allSquaresSum = []

def sumSquares(number):
    for i in range(number):
        numberSquare = i**2
        allSumSquares.append(numberSquare)
    return sum(allSumSquares)

def squaresSum(number):
    for i in range(number):
        allSquaresSum.append(i)
    return sum(allSquaresSum)**2
t = TicToc()
number = 11
t.tic()
print(squaresSum(number)-sumSquares(number))
t.toc()

t.tic()
nums=np.arange(1,11)
print(sum(nums)**2-sum(nums**2))
t.toc()

