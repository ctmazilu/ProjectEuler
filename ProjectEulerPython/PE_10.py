# Written 02/26/2021 by Christina Mazilu
# Project Euler Question 10: https://projecteuler.net/problem=10

allPrimes = []

def prime(n):
    for n in range(2,n):
        isPrime = True
        for i in range(2, n):
            if n % i == 0 :
                isPrime = False
        if isPrime:
            allPrimes.append(n)

    print(sum(allPrimes))

prime(10)
