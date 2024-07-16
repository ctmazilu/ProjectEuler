# Written 02/21/2021 by Christina Mazilu
# Project Euler Question 1: https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. Find the sum of all the multiples of 3 or 5 below 1000



total = []
for i in range(10):
    if i%3==0 or i%5==0:
        total.append(i)
print(max(total))
print(sum(total))


