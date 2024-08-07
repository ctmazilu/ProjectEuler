# Written 02/21/2021 by Christina Mazilu
# Project Euler Question 2: https://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

first = 0
second = 1
total = 0
fibi = [0]*1000
fibi[1]=1

def fib():
    first = 0
    second = 1
    total = 0
    while first < 4000000:
        first, second = second, first + second
        if first % 2 == 0:
            total += first
    print(total)

def fib_reccur(n):
    global fibi
    if n==0 or n==1:
        return n
    nt=fib_reccur(n-1)+fib_reccur(n-2)
    fibi[n]=nt
    return nt

fib()

#print(fib_reccur(11))
#print(sum(fibi[2:12]))
fib_reccur(35)

for f in (fibi):
    if (f < 4000000) and (f % 2 == 0):
        total += f

print(total)
