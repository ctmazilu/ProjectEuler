# Written 02/24/2021 by Christina Mazilu
# Project Euler Question 5: https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
# What is the smallest positive number that is evenly divisibl by all of the numbers from 1 to 20
def v2():
    i = 0
    flag = True
    while flag:
        i+=1
        if isDivisable(i):
            flag = False
    return i


def infinity():
    i=0
    while True:
        i+=1
        yield i

def smallestNumber():
    for number in infinity():
        if isDivisable(number):
            break
        else:
            number += 1
    return number

def isDivisable(number):
    for i in range(1,11):
        if number % i != 0:
            return False
    return True

number = smallestNumber()
print(number)

num = v2()
print(num)
