# Written 02/25/2021 by Christina Mazilu
# Project Euler Question 7: https://projecteuler.net/problem=7

# allPrime = []
#
# def infinity():
#     i = 0
#     while True:
#         i += 1
#         yield i
#
# def findPrime(n):
#     isPrime = True
#     for j in range(2, n):
#         if n % j == 0:
#             isPrime = False
#     return isPrime
#
# def listPrime(n):
#     for i in infinity():
#         if i > allPrime[n] and findPrime():
#             allPrime.append(i)
#             break
# listPrime(infinity())
# print(allPrime[number])

import numpy as np
nums=np.arange(2,120000)
plist=[]
while len(nums)>0:
    plist.append(nums[0])
    nums=nums[nums%nums[0]!=0]

print(plist[10000])
#print(len(plist))
