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

