def pf(number):
    primeFactor = []
    for i in range(2, number):
        if number % i == 0:
            isPrime = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
            if isPrime:
                primeFactor.append(i)
    print(max(primeFactor))

def pf2(number):
    primeFactor = []
    for i in range(2, number):
        if number % i == 0 and Prime(i):
              primeFactor.append(i)
    print(max(primeFactor))


def Prime(bu):
    isPrime = True
    for i in range(2, bu):
        if bu % i == 0:
            isPrime = False
    return isPrime

pf(13195)
pf2(13195)








